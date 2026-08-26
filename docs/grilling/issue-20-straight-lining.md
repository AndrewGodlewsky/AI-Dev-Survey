# Grilling — Issue #20: Straight-lining

**Ticket:** [Straight-lining: does the survey need attention checks, and where?](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20)
**Round:** 1 of ? — what straight-lining even looks like in *this* survey, and whether the reverse-keys really carry it
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What is already settled, and what I looked up

**Settled elsewhere and not re-asked here:**

- Block *ordering* and interleaving belong to [#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13). #6 already told #13 that interleaving the Coverage passes and Safeguard items between Dimension blocks is the cheapest mitigation. This ticket decides whether a **measure** is needed and of what class — not where blocks sit.
- Any planted item is unscored and costs length. The survey is **152 of 200** Forms questions and ~32–45 minutes — at the ceiling.
- A flag never excludes a person by rule. Every existing flag (`flag.malformed`, `flag.inconsistent-*`, `flag.hold`) means *go and ask*; #9's through-line is "refuse to compute at n=5–9 with named responses".

**Three facts that change the ticket's premise** (looked up in `survey/future-state-items.md`, `docs/research/microsoft-forms-export.md`, `scoring/scoring-rules.md`):

1. **The Future section is not "every item asked twice in a row".** #10 found Forms drops the Likert parent text, so #6's two-row blocks have to be built as **two separate 30-row Likert blocks** — all thirty `[Me] …` statements, then all thirty `[Team] …` statements — each block on one Desirability scale. So there are *two distinct* straight-lining shapes, not one:
   - **Flat-lining** — the same option down a 30-row block.
   - **Block-copying** — answering the `[Team]` block the way you answered the `[Me]` block, thirty rows earlier. This produces a Stance gap of exactly 0 on every Dimension, which is the one signal the two-stance design exists to produce. Nothing in the survey distinguishes a copier from a person genuinely aligned with the team.
2. **The reverse-keys dampen a flat-liner; they do not detect one.** Each Future block carries 7 reverse-keyed items (FC3, FT2, FF3, FG5, FN4, FA2, FV2) and 5 probes. I ran the arithmetic:

   | Flat answer down a block | 3-item Dimension score | Concern / Guardrails (5 facets) | Looks like… |
   |---|---|---|---|
   | **Definitely (5)** | (5+5+1)/3 = **3.7** | (4×5+1)/5 = **4.2** | a keen, slightly hedged adopter |
   | **Probably (4)** | (4+4+2)/3 = **3.3** | **3.6** | a moderate — perfectly plausible |
   | **Unsure (3)** | **3.0** | **3.0** | a fence-sitter — and *nothing* moves |
   | **Definitely not (1)** | **2.3** | **1.8** | a cautious sceptic |

   Every row of that table is a Dimension score a real person could hold. The contradiction is only visible **at the raw-item level** — seven reversed items all reading the opposite of the other twenty-three — and only if something *reads* them. Today nothing does: the sheet flips them and averages. So "the reverse-keys are the cheapest attention check" is true **only with a scoring-time rule attached**; without one they are a shock absorber, not a detector.
3. **The midpoint is a blind spot for the reverse-keys, full stop.** `6 − 3 = 3`. A person who answers *Unsure* to everything scores 3.0 on all seven Dimensions with a Gap of 0 and a Stance gap of 0, and the reverse-keys cannot tell. Only a pattern rule ("30 identical answers") can.

The Current section is a weaker case for all of this: 26 items on **two different scales** (9 behaviour, 17 attitude), broken up by the Coverage grid and a Safeguard item, so the 30-rows-of-one-scale shape does not occur there.

---

## Q1 — Which straight-lining are we actually guarding against?

### What this is

The ticket names one problem — fatigue — but fact 1 above splits it into two behaviours with different consequences. Before picking a measure, decide which behaviour(s) the measure is for.

### Why it matters

- **Flat-lining** corrupts a *person's* scores, and the reverse-keys already pull those toward the middle, so the damage is bounded (fact 2). At n=5–9 a flat-liner also shifts every team mean by up to a fifth of the distance to their flat value.
- **Block-copying** corrupts the *headline reading*. A team of nine where four copied the Me block into the Team block would show "mostly aligned" on the Stance page and the manager's overview — a finding, in the wrong direction, with no visible defect. And the reverse-keys are no help at all: a copier's contradictions are identical in both blocks, so the two blocks agree perfectly with each other.

There is a subtlety on block-copying: a Stance gap of 0 everywhere is also a *legitimate* answer ("I'd do exactly what I think the team should do"). At n=5–9 the difference is a conversation, not a rule — same as the inconsistent Safeguard answer in #19.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Both — flat-lining and block-copying** | Covers the headline reading, which is what the ticket is actually worried about. | Two different signatures, so probably two different checks. |
| **B. Flat-lining only** | Classic, well-understood; reverse-keys partially cover it. | Leaves the Stance gap — the design's reason to exist — undefended. |
| **C. Block-copying only** | Targets the one signal nothing else protects. | Lets the *Unsure* flat-liner through (they also block-copy trivially, so C catches them anyway — but only as a copier). |

### My recommendation

**A**, with the weight on block-copying. Flat-lining is already dampened; block-copying is not even noticed. If you want only one, take **C**: the *Unsure* flat-liner is a block-copier by construction, so C catches the worst flat-liner too.

### Your answer

: A

<!-- If you think a Stance gap of 0 across the board is simply a valid answer we should never second-guess, say so here — that would collapse Q1 to option B and change Q3. -->

---

## Q2 — Do the reverse-keys "carry it", now that we know they dampen rather than detect?

### What this is

The ticket offers "no, the reverse-keys carry it" as a real answer. Fact 2 says that answer has a hidden premise: something has to *read* the reverse-keyed items against their neighbours for a contradiction to surface. Fact 3 says even then, the midpoint is invisible.

So the honest form of the question is: **is dampening enough?** A flat-liner lands at 3.0–3.7 on every Dimension instead of at 5.0; their team-mean distortion is bounded; and at n=5–9 with named responses, a row of seven identical scores is something a human *might* notice on the People page.

### Why it matters

If dampening is enough, this ticket closes with "nothing — and here is why", the reverse-keys stay exactly as they are, and #13 inherits only the ordering advice it already has. If it isn't, Q3 becomes live.

The argument for "enough": named responses. Nobody straight-lines a survey their team lead will read with their name on it — social cost does what an attention check would. The argument against: the survey is *long*, the Future section is at the end of a 30-minute sitting, and the failure mode isn't malice, it's the 24th `[Team]` row at minute 38. Named or not, tired people flat-line, and *Unsure* is the tired answer.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Enough — close with "nothing"** | Zero cost. Consistent with "refuse to compute": don't manufacture a suspicion score. The pilot (#18) will show whether it happens at all. | Leaves the *Unsure* straight-liner and the block-copier undetected; the Stance page can show alignment that isn't there. Reverse-keys are then a shock absorber we call a check. |
| **B. Not enough — something must read the pattern** | Turns the reverse-keys into what the ticket already believes they are: a detector. Catches the midpoint case. | Something has to be built (Q3). Whatever it is must be a flag, never an exclusion. |
| **C. Enough for v1, revisit after the pilot** | Defers the cost until there is evidence. | The pilot is 1–2 people; it will not produce a flat-liner. "Revisit after the pilot" is "never" unless someone straight-lines the real run — by which point the sheet is built and the survey has gone out. |

### My recommendation

**B.** Not because I expect a flat-liner on a nine-person named survey, but because the *cost* of B is small if the measure is a scoring-time rule (Q3), and the cost of being wrong under A is the headline reading going upward in the wrong direction with no defect visible. C is A with a delay.

### Your answer

: B

<!-- If A: say whether you're happy for the map's Decisions-so-far to record "reverse-keys dampen but don't detect; accepted" — the one-pager already tells readers a 0 Stance gap is real, and this is the one place that claim could be wrong. -->

---

## Q3 — If something is needed, what class? *(Answer even if you picked A above — it records what you rejected and why.)*

### What this is

The ticket lists four classes. Two are **items** (cost length, must be unscored, visible to Respondents); two are **rules** (cost nothing at answer time, invisible to Respondents, land on the Scoring sheet and the flag family).

| Class | What it is | Where it lands |
|---|---|---|
| **Planted check item** | "Please answer *Probably* to this row." | Survey (#13); unscored; +2 rows (one per stance block) |
| **Repeated item** | Ask one stem twice, far apart, compare. | Survey (#13); unscored; +2 rows; needs a comparison rule anyway |
| **Detectable-pattern rule** | Sheet computes per block: modal-answer share, longest identical run, count of reverse-keyed items agreeing with the block's mode; and Me-vs-Team identical-row count. Raises a flag. | Scoring sheet (#15), `flag.*` family (#12), People page (#16) |
| **Nothing** | — | — |

### Why it matters

Two of this survey's standing rules cut hard against the item classes:

- **Non-leading, gut-reaction, no item may push a Respondent toward a position.** A planted "answer *Probably* here" is, precisely, an instruction to hold a position. On a named survey to peers it also reads as *we don't trust you to read* — which is a message this survey should not send in a section that is asking people to be honest about their edges.
- **Every statement text in the form must be unique** (#10), so a repeated item can't be a literal repeat; it has to be a paraphrase — and then a mismatch is "the paraphrase was different", not "the person wasn't reading". The T1/T2 belief-vs-behaviour pair is already the honest version of this.

Against the rule class: it's one more thing #15 must build formula-only, and thresholds are a judgement (a 30-row block with 27 identical answers — is that a flat-liner or a genuine *Definitely* adopter? Reverse-keys answer that: a genuine adopter answers the seven reversed rows *differently*). Threshold and wording are round 2; class is the decision here.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Detectable-pattern rule only** — a flag per block (`flag.flat-<pass>`) plus a Me/Team block-copy flag, computed on the sheet, shown on the People page, "go and ask" | Zero survey cost. Invisible to Respondents. Reads the reverse-keys, which is what the ticket already assumed was happening. Catches the *Unsure* case and block-copying. Same flag semantics as #19. | Thresholds to decide (round 2). One more formula family for #15. A flag on a named person needs the one-pager's "position, not fault" framing — actually *stronger* here, because "you weren't paying attention" is closer to a fault. |
| **B. Planted check item(s)** | Unambiguous when tripped. | Violates the non-leading rule; reads as distrust; +2 rows at the ceiling; still doesn't catch block-copying unless it's a *different* instruction in each block. |
| **C. Repeated item + comparison rule** | Feels rigorous. | Can't be a true repeat (#10 uniqueness); a paraphrase mismatch is ambiguous; +2 rows; still needs a rule, so it is A plus cost. |
| **D. Nothing** | Free. | Only coherent with Q2 = A. |

### My recommendation

**A.** It is the only class that (i) costs no rows, (ii) doesn't lead, (iii) catches the midpoint, and (iv) catches block-copying. It also makes the map's existing sentence true — "the reverse-keys are the cheapest attention check" becomes a fact rather than a hope. The flag semantics are already designed: `1` = go and ask, never excluded, never scored.

### Your answer

: A

<!-- If A: round 2 will put to you (a) the exact signatures and thresholds, (b) whether the flag is one column or one per block, (c) how the dashboard shows it — internal only, presumably — and (d) whether a flagged person's Stance gaps still render on the Team overview. -->

---

## Q4 — What does a straight-lining flag *do* to the numbers? *(Principle, independent of class.)*

### What this is

Every existing flag leaves the numbers alone: a malformed row is excluded because it *cannot* be computed, an inconsistent Safeguard answer withholds Levers because they *cannot* be derived, but no flag has ever said "this person's answer is computable but we doubt it". A straight-lining flag would be the first flag of that kind.

### Why it matters

If the flag excludes, the sheet is now making a judgement about a named colleague's honesty by formula — and at n=7 removing one person moves every team mean. If the flag doesn't exclude, a genuine flat-liner's 3.0s sit in the team means and the "mostly aligned" Stance count until someone acts on the flag. The one-pager's entire stance is *show the points, don't summarise, go and ask*.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Flag only — numbers untouched, visible marker on the People page and beside the person in the Layered view, "go and ask"** | Consistent with every other flag and with "refuse to compute". No formula judges a colleague. Recovery is the same as malformed: a conversation, possibly a re-take of one block. | Until the conversation happens, the numbers include the suspect row. |
| **B. Flag and exclude from team statistics, like a malformed Dimension** | Team numbers are clean immediately. | A formula has decided a named person didn't mean their answers. At n=5–9 that is a big lever for a threshold to hold. Nobody is excluded today except for genuinely missing data. |
| **C. Flag, and withhold only the Stance gaps** (the reading block-copying corrupts), leaving Dimension scores in | Targets the actual damage. | Half-measure with its own explanation cost; still a formula judging intent. |

### My recommendation

**A.** The flag is a pointer to a conversation. If the conversation confirms it, the fix is the same as a blank: the person re-takes the block or is left out *by a human*, and `flag.malformed`-style exclusion already exists for that. The sheet should never decide a colleague was not paying attention.

### Your answer

: A

---

## Anything else

Anything this round has wrong, or a constraint I haven't seen — e.g. whether Forms lets you shuffle statement order inside a Likert (I did not find a source either way, and it would matter for #13, not here), or whether you'd rather this ticket also cut the ten optional Future rows #6 left on the table.

### Your answer

: 

---
---

# Round 2 — the rule itself: scope, signatures, thresholds, columns, display

**Round:** 2 of ? — probably the last.
**How to use:** same as round 1.

## Read-back of round 1

| | You said | So |
|---|---|---|
| **Q1** | **A** — guard against both flat-lining and block-copying | Two signatures, not one. |
| **Q2** | **B** — dampening is not enough; something must read the pattern | The ticket does **not** close with "nothing". "The reverse-keys are the cheapest attention check" becomes true by adding the reader. |
| **Q3** | **A** — a scoring-time detectable-pattern rule; no planted or repeated item | Survey length and wording untouched. #13 inherits nothing new. Lands on #15 (formulas), #12 (columns), #16 (display). |
| **Q4** | **A** — flag only; numbers untouched; "go and ask" | Same semantics as `flag.inconsistent-*`. A formula never judges a colleague's intent; a human resolves it, and `flag.malformed`-style exclusion already exists if a re-take is refused. |

Nothing under *Anything else*, so the round-1 facts stand: two 30-row Future blocks; 7 reverse-keyed items and 5 probes per block; the midpoint is invisible to reverse-keys.

**Taken as routine, not asked:** resolving this ticket amends the closed `#12` schema (`scoring/scored-csv-schema.md` gains the columns decided below, `scoring/scored-sample.csv` and its generator carry them, and one sample persona is made to trip each flag so #15 has an acceptance row). The dashboard loader already treats unknown-optional columns as a warning, not a refusal, so this is additive.

---

## Q5 — Which blocks does the flat-lining rule read?

### What this is

The rule needs a defined set of rows per Respondent to look at. The candidates, with their shape:

| Block | Rows | One scale? | Reverse-keys to read? |
|---|---|---|---|
| **Future — `[Me]`** | 30 (25 items + 5 probes) | Yes, Desirability | 7 |
| **Future — `[Team]`** | 30 | Yes, Desirability | 7 |
| **Current — attitude items** | 17 | Yes, Attitude | 5 (C3, F3, G6, N4, V2) |
| **Current — behaviour items** | 9 | Yes, Behaviour | 2 (T2, A2) |
| **Coverage grid, each pass** | 19 | Yes, Involvement 1–6 + N/A | **None** |

### Why it matters

The Future blocks are the case the ticket was filed for. The Current attitude block is 17 rows on one scale — shorter, earlier in the sitting, but the same shape. The behaviour block is 9 rows and carries almost no reverse-keys, so a pattern there is weak evidence. The Coverage grid has **no reverse-keys and a legitimate flat profile** — someone who is "Doer, reviewed" on all 19 areas is a coherent person, not a tired one — so a rule there would flag honest answers.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Future `[Me]` and `[Team]` only** | Exactly the ticket's case. Two blocks, same size, same scale, same reverse-key count — one formula copied twice. | A 17-row flat-line in the Current attitude block goes unread. |
| **B. A plus the Current attitude block** | Same rule, third copy, with `n` = 17 and 5 reverse-keys; catches the earlier block too. | Thresholds have to be expressed as fractions, not row counts, to work on 30 and 17. Slightly more #15 work. |
| **C. Every Dimension-item block including behaviour** | Complete. | The 9-row behaviour block has one usable reverse-key; a "flag" there is noise. |
| **D. Everything including the Coverage grids** | — | Flags legitimate profiles. No reverse-keys to corroborate. |

### My recommendation

**B.** The rule is the same formula either way, so covering the 17-row attitude block costs one more copy and buys the only other block with the flat-lining shape. Coverage is out on principle: a flat Involvement profile is a real position.

### Your answer

: B

---

## Q6 — The flat-lining signature and its threshold

### What this is

Per block, what the sheet computes and when it raises the flag. Two statistics are cheap in formulas and together cover both the reverse-key case and the midpoint case:

- **Modal share** — the fraction of the block's rows answered with the block's most common option. A tired *Unsure* down 30 rows = 1.00. This is the only thing that catches the midpoint.
- **Reverse-key agreement** — of the block's reverse-keyed items, how many were answered with the **same raw option as the block's mode**. A person who genuinely holds the block's modal position answers the reversed rows *away* from the mode (a "Probably" adopter answers "…keep doing things by hand" with *Probably not*). Agreement therefore means the reversed rows were not read. Probes are excluded from this count (never reverse-keyed) but included in the modal share (they are rows).

Then the flag is a threshold on those two. The threshold is the judgement; it should be strict enough that a genuine extreme adopter is not flagged and loose enough that a tired *Probably* is.

Worked cases on a 30-row Future block, 7 reverse-keys:

| Person | Modal share | Reverse-key agreement | Should flag? |
|---|---|---|---|
| Flat *Probably*, every row | 30/30 = 1.00 | 7/7 | yes |
| Flat *Unsure*, every row | 1.00 | 7/7 | yes (midpoint case) |
| Genuine strong adopter: 23 non-reversed rows *Definitely*, 7 reversed rows *Definitely not* | 23/30 = 0.77 | **0/7** | **no** |
| Tired-in-the-second-half: 15 considered rows, then *Probably* ×15 including 4 of the reversed rows | ~0.6 | 4/7 | borderline — probably no |
| Mostly *Probably* with a few *Unsure*, reversed rows also *Probably* | 0.85 | 6/7 | yes |

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Two-part rule: flag when reverse-key agreement ≥ 6 of 7 (≥ 4 of 5 on the 17-row block) — OR modal share ≥ 0.90** | The reverse-key part is the strong evidence and is proportion-free; the modal-share part exists only for the midpoint. A genuine extremist never trips either. | Two numbers per block to explain. |
| **B. Modal share only, ≥ 0.90** | One number. | Misses the tired *Probably* who happened to vary a few rows (0.85, 6/7 agreement) — the most likely real case — while flagging nothing a reverse-key would have caught earlier. |
| **C. Reverse-key agreement only, ≥ 6 of 7** | One number, and the one that reads the reverse-keys as the ticket assumed. | Blind at the midpoint: *Unsure* ×30 gives 7/7 agreement — so actually it **does** catch it, because 3 = mode = reversed answer. The only miss is a person who varies among 2/3/4 but keeps the reversed rows at the mode… which is exactly a flat-liner. Real gap: a block with *two* modes. |
| **D. Same as A but the thresholds are input cells on the sheet** | The threshold is a judgement; making it a cell lets the pilot tune it without touching formulas. | One more thing on the sheet to document. |

### My recommendation

**D** — the two-part rule from A, with the two thresholds in named input cells (defaults 6 of 7 / 0.90) so #18 can tune them on real data. C is nearly as good and simpler; if you want one number, take C. And in every case the **statistics themselves are exported**, not just the flag — Q8.

### Your answer

: D

---

## Q7 — The block-copying signature and its threshold

### What this is

Block-copying is one signature: **on how many of the 30 stems did `[Team]` receive the same option as `[Me]`?** Call it *stance-identical count*. The Stance gap on every Dimension is 0 exactly when it is 30/30 (probes aside).

The complication from round 1 stands: 30/30 is also a *legitimate* answer — "I'd do exactly what I think the team should". Only a person can tell the two apart, which is why this is a flag and not an exclusion (Q4). The threshold question is only *how identical* before we ask.

Note the two Coverage grid passes (`6 months, me` / `6 months, the team`) have the same shape — 19 areas — and copying there is just as plausible. But a Coverage Stance gap of 0 is a much weaker claim (levels are coarse, and "the team should do what I do" per area is ordinary), so I'd keep the rule to the Dimension blocks.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Flag at 30 of 30 identical** | Zero false positives on anyone who thought about even one row. | A copier who changed one row by accident escapes. |
| **B. Flag at ≥ 28 of 30 (≥ 0.93)** | Catches the near-copier. | Starts flagging a genuinely aligned person who differed on two items — but that is exactly the conversation worth having, and the flag is "go and ask". |
| **C. Export the count, no flag — the dashboard shows it and a human eyeballs** | No threshold to defend. | A count nobody is told to look at is not a check. Q2 said something must *read* the pattern. |
| **D. B, threshold in an input cell (default 28)** | Consistent with Q6-D. | — |

### My recommendation

**D.** Export the count *and* flag at a tunable threshold, default 28 of 30. Coverage grids excluded for the reason above.

### Your answer

: D

---

## Q8 — What travels in the Scored CSV?

### What this is

#12 fixed one flag family (`flag.*`, 0/1 or item lists). This ticket adds to it. Two shapes:

| Shape | Columns | Count |
|---|---|---|
| **Flags only** | `flag.flat-current` · `flag.flat-future-personal` · `flag.flat-future-team` · `flag.stance-identical` | 4 |
| **Statistics + flags** | the 4 flags **plus** `pattern.modal-share.<pass>` (×3), `pattern.reverse-agree.<pass>` (×3, as a count), `pattern.stance-identical` (count of 30) | 4 + 7 = 11 |

(If Q5 = A, drop the `current` columns: 3 flags, 3 + 5.)

### Why it matters

#9's principle is *show the points, not the summary*. A bare flag is a summary of a judgement; the statistics let the People page say "28 of 30 identical; reversed rows 6 of 7 at the mode" so the conversation starts from facts. It also means a threshold tuned after the pilot (Q6-D/Q7-D) can be re-applied by the dashboard without re-exporting. The cost is seven more columns on a 279-column file.

The dashboard computes team statistics only (#12's seam) — these are per-Respondent, so they must come from the sheet, not be recomputed from raw items in the browser. (The raw items *are* in the CSV, so the dashboard *could* recompute them; but then two implementations of one rule must agree, which is the thing the seam exists to avoid.)

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Statistics + flags (11 columns; `pattern` is a new family, flags join `flag`)** | Facts travel with the judgement. Threshold-independent record. | +11 columns; schema doc and generator updated. |
| **B. Flags only (4 columns)** | Minimal. | The People page can only say "flagged", not why; a tuned threshold needs a re-export. |
| **C. Statistics only, no flags — dashboard applies the threshold** | Threshold lives in one place (the dashboard). | Breaks the seam: the sheet is where per-Respondent judgements live, and a hand-scorer working from RUBRIC.md would have no rule to apply. |

### My recommendation

**A.** Eleven columns is cheap; a flag without its evidence is the thing this survey keeps refusing to produce.

### Your answer

: A

---

## Q9 — Where the dashboard shows it

### What this is

Q4 fixed that the numbers are untouched. This is only *where a person sees the flag*. Existing precedent: `flag.malformed` shows on the People page, beside the person in the Layered view, and as an **unnamed count** on the Team overview ("2 malformed excluded"); `flag.inconsistent-*` shows on the People and Safeguards pages, and as a count in the export line.

A straight-lining flag is different in one way: "malformed" reads as *the export broke*; "flat-lined" reads as *you didn't pay attention*. It is closer to a fault than any existing marker, and this survey's one-pager promises markers never are.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Internal view only: People page (with the statistics), a marker beside the person in the Layered view and Stance page. Team overview and exported view say nothing.** | The flag's job is to be resolved *before* anything goes upward — like a blank. Nothing that could read as a fault reaches the manager. | If a flag is never resolved, the exported numbers silently include the suspect row. That is Q4-A's accepted cost. |
| **B. A, plus an unnamed count on the Team overview ("1 response flagged for straight-lining — unresolved")** | Honest: the manager sees the numbers carry a caveat. | A count of one on a team of seven is a name. And it advertises a colleague's fatigue upward. |
| **C. A, plus a banner on the *internal* view only when any flag is unresolved — "resolve before exporting"** | Nudges the team to do the conversation before printing, without anything going upward. | One more UI state. |

### My recommendation

**C.** The flag exists to trigger a conversation before the export; a banner on the internal view is the reminder, and the exported view stays clean. Wording on the People page should follow the one-pager: *"Answers follow a pattern the reverse-keyed items don't support — worth a conversation before the results go upward."* Never "straight-lined".

### Your answer

: C

---

## Anything else (round 2)

Anything to add before I write the resolution — in particular whether the term should enter `CONTEXT.md` (I'd propose **Pattern flag** — *a non-scoring per-Respondent marker raised when a block's answers follow a pattern its reverse-keyed items don't support; locates a conversation, never a fault*), and whether you want the two thresholds written into `rubric/RUBRIC.md` §6 so a hand-scorer applies the same rule as the sheet.

### Your answer

: 
