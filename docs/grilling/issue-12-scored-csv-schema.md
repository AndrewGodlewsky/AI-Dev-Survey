# Grilling — Issue #12: Scored CSV schema

**Ticket:** [Scored CSV schema: the contract between the Scoring sheet and the dashboard](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12)
**Round:** 1 of ? — the shape of the file
**How to use:** answer inline under each `### Your answer` heading. Free text is fine; you don't have to pick one of the listed options. Then tell me it's ready and I'll read it back and compute the next round.

---

## What is already settled, and what I checked

The ticket sketches a **long** format — one row per Respondent × measure, columns `kind (dimension | area), name, section, stance, score`. Two constraint comments landed on it since:

- **#8 (Probe items):** Edge markers are a non-scoring per-Respondent attribute, tracked per stance row, and the long sketch has nowhere to put them. Probe answers must be excluded from every Dimension mean, so if raw answers travel they must be *distinguishable*.
- **#19 (Safeguard items):** the same slot must carry accepted safeguards × three askings, Levers (derived), learning interest, and the inconsistency flag — **per Respondent, not per Dimension**. "Belongs to neither `dimension` nor `area`."

Two more inputs exist now that didn't when the ticket was written:

- **#9 §8** lists what the CSV must carry: 7 × 3 Dimension scores, facet values, 19 × 3 Involvement levels, the non-scoring family, and the malformed-export flag.
- **#11 (prototype, closed)** is the CSV's consumer. Its `scorePerson` / `teamDim` / `teamArea` functions read a fixed set of named fields per person — nothing generic. The dashboard already resolves everything by name.

Facts I looked up rather than asking (they shape the recommendations below):

| Fact | Consequence |
|---|---|
| Excel *Save as CSV* writes **one sheet** per file | "One CSV" means one sheet in the Scoring workbook is *the export*; several CSVs means several sheets and several saves. |
| Excel writes numbers **as displayed** — a cell formatted to 1 dp exports 1 dp | The export sheet must keep score cells in General format, or we ship rounded Gaps — the exact failure #9 §2.4 forbids. |
| On a Windows locale whose list separator is `;`, "CSV (comma delimited)" still writes `;` | The dashboard should sniff the delimiter; #15's save instructions should name "CSV UTF-8". |
| A dashboard opened from disk cannot `fetch()` a sibling file | The CSV arrives by file-picker or drag-drop. One file = one drop; three files = three drops, every time. |
| Forms exports answers as **label text** (#10) | Someone converts labels to numbers. The sheet already must (it scores them); the question is whether the CSV carries the numbers or the labels. |

---

## Q1 — Wide or long?

### What this is

**Long** (the ticket's sketch): one row per Respondent × measure, ~250 rows per person, generic columns. **Wide**: one row per Respondent, ~250 named columns grouped in families (`comfort.cur`, `area.04.ft`, `safe.fp.3` …).

### Why it matters

This is the decision everything else hangs off — column names, how the sheet builds the export, how the dashboard loads it.

Long format is the right shape for *generic* charting code: a tool that doesn't know the domain can group by `kind` and `name`. That is not our situation. The prototype reads `scores.trust.fp`, `cov[13].ft`, `safe.fp` — every view knows exactly which field it wants. And long format has already failed the domain twice: Edge markers and Safeguards don't fit `kind × name × section × stance × score`, which is why #8 and #19 had to leave comments. Each new attribute class would need a new `kind` and a reinterpretation of the other columns.

In a **formulas-only** workbook, wide is also what the sheet naturally produces: the scored sheet is one row per Respondent with one formula per cell, and that sheet *is* the export. Long format would need row-generating formulas (INDEX over a fixed 9 × 250 template) that nobody can debug without VBA.

The honest cost of wide: a wide header row is ~250 names, and the contract lives in those names. They have to be systematic, and the dashboard has to resolve by header (never position — the rule #10 already imposed on the Forms export).

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Wide** — one row per Respondent, named column families | One formula per cell in the sheet; the scored sheet is the export. Every attribute class (scores, levels, probes, safeguards) is just another family — no schema contortion. Matches how the consumer already reads data. | ~250 columns; the names *are* the contract and must be systematic. Adding a Dimension later adds columns (fine) rather than rows. |
| **B. Long** — the ticket's sketch, extended | Generic; a spreadsheet pivot or any BI tool reads it. Adding a measure adds rows, not columns. | Already broke twice on non-scoring attributes; would need `kind ∈ {dimension, area, probe, safeguard, …}` with the other columns meaning different things per kind. Hard to produce with formulas only. The dashboard would pivot it straight back to wide. |
| **C. Both** — wide for the dashboard, long as a second sheet for ad-hoc analysis | Ad-hoc pivots stay easy for the pilot analysis (#6 wants to see which item pairs never diverge). | Two contracts to keep in step; two saves. The pilot analysis can pivot inside Excel from the wide sheet anyway. |

### My recommendation

**A.** Long format's one advantage — generic consumers — is one we don't have and #6's pilot analysis can be done in the workbook. Wide is what both ends of the contract naturally speak.

### Your answer

: ok let's go with long

<!-- If B or C: which consumer, other than the dashboard, needs the long shape? -->


---

## Q2 — Where is the line between the Scoring sheet and the dashboard?

### What this is

Who computes what. The sheet must compute Dimension scores (the facet map lives there — #9 §8 says so). Beyond that, everything from Gap to team means could sit on either side.

### Why it matters

Two things pull in opposite directions.

**Single source of truth.** #14's Rubric is done "when someone could score a response by hand from it", and #15's sheet is the executable form of that. If the dashboard re-derives *anything* per Respondent — even a subtraction — there are two implementations of a rule, and when they disagree nobody knows which is right. The Lever rule (excluded when inconsistent), the reverse-keys, the Guardrails collapse: each is a place two implementations can drift.

**The lens.** Team-level numbers change when the dashboard filters by Context tool: mean, range, median, counts, draft norms, `n` are all functions of *which* Respondents are in view. Those cannot be pre-computed in the sheet without exporting every possible filter.

So the natural seam is **per-Respondent vs per-team**: everything that is a fact about one person is computed once, in the sheet; everything that aggregates people is computed live, in the dashboard. The seam is also exactly the export-split line from #9 §4.1 — per-Respondent values are individual results; team aggregates are what the manager sees.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Sheet computes every per-Respondent value; dashboard computes only team aggregates** — scores, Gap, Stance gap, Coverage gaps (signed steps or `NA`), Levers, principle hold, inconsistency flags, probe Edge markers all in the CSV | One implementation of every rule, in the artifact the Rubric describes. Dashboard code is aggregation and rendering only. Someone with no dashboard can still read a person's Gap off the CSV. | More columns (~40 derived). The sheet must implement the Lever exclusion and the Edge-marker threshold — both trivial. |
| **B. Sheet exports scores and raw levels only; dashboard derives the rest** | Smallest CSV. Sheet formulas stay to the facet map. | Every derived rule exists twice (Rubric prose + JS) with no executable check that they agree. The CSV alone can't answer "what is this person's Gap". |
| **C. Sheet also pre-computes team aggregates for the unfiltered view** | Team numbers are in the file for anyone without the dashboard. | Wrong the moment a lens is applied; two sources for the same team mean. The dashboard would ignore them. |

### My recommendation

**A.** With one exception folded in: Coverage Edge markers (level 6 on a high-stakes area) are *not* duplicated as columns — the level *is* the marker, the high-stakes list is six fixed areas, and a copy would be a second place to get out of step. Probe Edge markers *are* exported, because the 4–5 threshold is a rule, and rules live in the sheet.

### Your answer

: let's go with A

<!-- If B: is it sheet complexity you're avoiding, or CSV width? -->


---

## Q3 — One CSV, or a second manager-flavoured one?

### What this is

#9 §4.1 splits the views: internal keeps names; the exported team view carries mean, range, `n` and **unnamed counts** — never individual rows. Does that split produce a second CSV?

### Why it matters

Stripping the `respondent` column from this CSV does **not** produce a manager-safe file: each row is still one person, and at n=7 the row *is* the individual result. A genuinely manager-safe CSV would be **pre-aggregated counts** — a completely different schema (one row per Dimension × level × pass, one per area × level × pass), produced by a second sheet, saved separately, and loaded into a dashboard that would then need two code paths.

The prototype settled the other route: the dashboard's **Exported team view** and **Team overview** render counts from the named data, and the manager receives the *rendered* page — printed, PDF, or the dashboard opened in export mode. #16 and #17 own that; the CSV doesn't.

The one thing that argues for a second file: if the manager is handed the HTML dashboard *and* a data file, the data file must be safe. That is a #16 question ("does the manager get the dashboard or a rendering?") and it can be answered there without the CSV growing a second schema now.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. One CSV, always named, always internal.** The manager view is a rendering concern for #16/#17. | One schema, one save, one drop. The export split is enforced where it is visible — on the page. | The CSV itself must never travel upward; a process rule, not a technical one. |
| **B. Two CSVs: named (internal) and pre-aggregated counts (manager)** | A manager-safe data file exists. | Second schema, second sheet, second save, second loader; the counts file is wrong the moment a lens is applied; and the residual re-identification #9 states still applies to counts. |
| **C. One CSV plus a `share` flag column per row** | Cheap. | Meaningless — a row is a person; there is no per-row way to make it a team fact. |

### My recommendation

**A.** Carry to #16: decide whether the manager receives a rendering or the dashboard + a counts file; if the latter, that counts file is *#16's* export, generated by the dashboard from the loaded data, not a second contract on this ticket.

### Your answer

: A

<!-- Does the manager ever get a *file* from you, or only something they look at? -->


---

## Q4 — Do raw item answers travel?

### What this is

Whether the CSV carries the 26 current + 25 × 2 future scored answers and the 5 × 2 probe answers as columns, or only the scores derived from them.

### Why it matters

Drill-down is the stated reason in the ticket. But the prototype's person profile never showed items — it showed Dimension scores, the Coverage strip, safeguards and Edge markers, and that was enough for the reaction rounds. So the dashboard case for items is weak.

Two other cases are stronger. **Probes:** the dashboard needs each Respondent's probe *answers* per stance to render the three Edge states — that's the raw answer, not a score, so at least ten "item" columns travel regardless. **The pilot:** #6 deferred a 10-row reduction "until the pilot shows which item pairs never diverge" — an item-level analysis. It can be done in the workbook, but a CSV that already has the items lets it be done anywhere, including by the dashboard later.

There is also a subtle choice inside "include": **as answered** (1–5, before reverse-keying) or **as scored** (after `6 − answer`). As-answered is a faithful record of what the person said; as-scored is what the mean used. Exporting as-scored means the CSV contains numbers that don't match the Forms export for seven items per section, which is a trap for anyone cross-checking by hand.

Facet values are a third candidate. They are the unit #9 §2.2 scores by, but they are pure arithmetic over items — derivable, and the only non-trivial one (Guardrails G2/G3) is the sort of thing the sheet already shows.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Items as answered + probes as answered; no facet columns** | Faithful record; matches Forms by eye; probes distinguishable by family so nothing averages them; pilot analysis possible from the CSV. | ~86 more columns. Reverse-keying is invisible in the CSV — it lives in the sheet and the Rubric. |
| **B. Scores and probes only** | Smallest file that still renders every prototype view. | Any item-level question means going back to the workbook. |
| **C. Items as scored (post reverse-key) + facets** | Everything the mean used is visible. | Seven items per section disagree with the Forms export by eye; facets are redundant with the scores. |

### My recommendation

**A.** Width is free; ambiguity isn't. Items travel exactly as the person answered them, probes travel in their own family, and the only transformation the CSV shows is the one that matters — the scores.

### Your answer

: A

<!-- If B: are you sure the pilot's "which pairs never diverge" check is happy living in Excel only? -->


---

## Anything else

<!-- Free space. Constraints on file naming, where the CSV lives in the repo, anything about how the sheet will be operated by whoever isn't you. -->


---
# Round 2 — long, with eyes open; then how values are written

**Read-back of round 1:** Q1 **long**. Q2 **A** — the sheet computes every per-Respondent value, the dashboard only aggregates. Q3 **A** — one CSV, always named, always internal; the manager gets a rendering. Q4 **A** — items and probes travel as answered; no facet columns.

Q1 went against the recommendation, which is fine — but Q2-A and Q4-A change what *long* costs, and the ticket's sketch was written before either existed. Q5 lays the result out so the choice is confirmed against the real shape rather than the sketch. Q6–Q9 are about how individual values are written and hold under either shape.

---

## Q5 — Long, concretely: confirm or flip

### What this is

What one Respondent's slice of a **long** file looks like once Q2-A and Q4-A are applied. Column set (names provisional until round 3):

```
respondent, kind, name, section, stance, value
```

| kind | name | section | stance | value | rows / person |
|---|---|---|---|---|---|
| `context` | tool key | — | — | 1–4 | 5 |
| `item` | C1 … V3, FC1 … FV3 | current / future | — / personal / team | 1–5 as answered | 26 + 50 |
| `probe` | P1 … P5 | future | personal / team | 1–5 as answered | 10 |
| `dimension` | comfort … craft | current / future | — / personal / team | score, full precision | 21 |
| `gap` | comfort … craft | — | personal (Gap) / stance (Stance gap) | signed decimal | 14 |
| `area` | 19 area keys | current / future | — / personal / team | 1–6 or `NA` | 57 |
| `area-gap` | 19 area keys | — | personal / stance | signed integer or `NA` | 38 |
| `edge` | P1 … P5 | future | personal / team | 0/1 | 10 |
| `safeguard` | 7 safeguard keys | current / future | — / personal / team | 0/1 | 21 |
| `lever` | 7 safeguard keys | — | — | 0/1 (or `NA` if inconsistent) | 7 |
| `learn` | 7 safeguard keys | — | — | 0/1 | 7 |
| `flag` | inconsistent-current, inconsistent-future-personal, inconsistent-future-team, hold, malformed | — | — | 0/1, or item list | 5 |

**≈ 271 rows per Respondent; ≈ 2,440 rows at n = 9.**

### Why it matters

Three things follow from that table that weren't visible from the sketch.

**The workbook needs the wide sheet anyway.** Dimension scores are means over facets of specific items; a formula for `trust.current` reads `T1, T2, T3` from *columns* of the Forms import. So #15 builds a wide "scored" sheet regardless. Under long, the export is a **second** sheet: a fixed template of 2,440 pre-built rows (respondent index × the 271-row measure list), each row an `INDEX`/`MATCH` into the wide sheet. That is ~2,440 formulas whose only job is reshaping — and every measure added later means adding rows to the template, not one column. Under wide, the scored sheet *is* the export and the second sheet doesn't exist.

**`section` and `stance` don't mean the same thing on every row.** `item` rows use both; `gap` rows use `stance` to mean "which Gap" (personal Gap vs Stance gap); `lever`/`learn`/`flag` rows use neither. A generic reader has to know the kind to interpret the other columns — which is the long format's promise ("generic") quietly failing. It's workable; it's just a contract with twelve sub-contracts.

**The dashboard pivots it straight back.** Every view reads `scores.trust.fp`, `cov[13].ft`, `safe.fp` — per person. The first thing the loader does with a long file is group by `respondent` and rebuild the wide object. That's ~20 lines of JS, not a real cost — but it means nothing on the consumer side wants long.

What long genuinely buys: a file a spreadsheet pivot or any BI tool reads without knowing the domain, and a shape where a new measure is a new row-set rather than a new column-set. If either of those is a real need — you plan to pivot this in Excel or Power BI, or you expect the measure list to keep changing — long is the right call and the template cost is paid once.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Confirm long** — the table above, template sheet in #15 | Generic, pivot-friendly, row-extensible. | ~2,440 reshaping formulas; per-kind meaning of `section`/`stance`; the dashboard un-pivots it on load. |
| **B. Flip to wide** — one row per Respondent, the same twelve families as column-name prefixes (`item.C1`, `dimension.trust.future.team`, `area.13.current`, `safeguard.tests.future.personal`, `flag.hold` …) | The scored sheet is the export; no template; every column has one meaning; matches the consumer. | ~270 columns; a new measure is a new column in the sheet and the loader. |
| **C. Long, but only for measures — items/probes/safeguards stay wide in a second file** | Smaller long file. | Two files, two schemas, two drops. Worst of both. |

### My recommendation

**B**, unless you have a pivot/BI use in mind that you haven't mentioned — in which case say so and A stands. Either answer is fine; the rest of the design only needs it to be *decided*.

### Your answer

: let's go with your recomendation

<!-- If A: what will read the long file besides the dashboard? -->


---

## Q6 — Score precision

### What this is

Dimension scores are means over facets — `3.6666…`. How many decimals the CSV carries, and whether that is enforced in the sheet or the dashboard.

### Why it matters

Excel exports numbers **as displayed**. If the export sheet formats score cells to one decimal for readability, the CSV carries `3.7`, and every Gap the dashboard computes from it is rounded-before-subtraction — the exact failure #9 §2.4 rules out. The same applies to Gap and Stance gap cells the sheet exports directly. The rule has to be stated on #15, not assumed.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Full precision, General format; the dashboard rounds to 1 dp for display only** | Nothing is rounded before a subtraction anywhere. The CSV is the unrounded truth. | Ugly numbers in the raw file; whoever opens the CSV in Excel sees `3.66666666666667`. |
| **B. Sheet rounds to 2 dp on export** | Readable file; 2 dp is below anything the dashboard shows. | A rounding step exists; on a 5-facet mean it can shift a Gap by 0.01 — harmless, but #9 said "never", and a 2-dp rule invites a later 1-dp "tidy-up". |
| **C. Sheet rounds to 1 dp** | Matches display. | Manufactures movement; the Gap of 1 for a 0.2 move is exactly this. |

### My recommendation

**A.** Readability belongs to the dashboard and the Rubric, not the interchange file.

### Your answer

: A

<!-- -->


---

## Q7 — Malformed answers in the file

### What this is

#9 §2.5: a blank Dimension item is a malformed export; the score reads `#N/A`, visibly, and nothing averages around it. How that reaches the CSV.

### Why it matters

Excel writes an `#N/A` cell to CSV as the literal text `#N/A`. Any numeric parser fails on it — loudly, which is what we want. But "the Trust score is `#N/A`" tells the dashboard *that* something is broken, not *which item* was blank, and the recovery is a conversation with a named person about a specific question.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. `#N/A` in every affected score/gap cell, plus a `malformed` flag carrying the blank item IDs** (e.g. `T2;N4`) | Fails loudly *and* says where. Dashboard can show "Trust — malformed (T2 blank)". | One more derived value in the sheet (a `TEXTJOIN` over blank checks). |
| **B. `#N/A` only** | Nothing extra. | The dashboard says "broken", someone opens the workbook to find out why. |
| **C. Empty cell** | Looks tidy. | Empty means nothing; parsers turn it into 0 or skip it. The failure #9 is trying to make impossible. |

### My recommendation

**A.**

### Your answer

: A

<!-- -->


---

## Q8 — Coverage "I don't do this work"

### What this is

The grid's N/A is real data, not a blank: excluded from the profile, counted. How it is written.

### Why it matters

Whatever token is chosen must be impossible to confuse with a malformed blank (Q7) and impossible for a careless tool to average. `0` fails the second test — a mean over `0, 3, 4` is a number that looks like a level. An empty cell fails the first. A literal token fails neither, and the same token can serve the derived cells: a Coverage Gap for a mixed `N/A → level` pair is "no Gap", which #9 §5.3 says must be *counted and flagged, never silent* — the dashboard derives the flag from the two pass values, so the gap cell just needs to say "not a number".

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Literal `NA`** for levels; `NA` for any Coverage Gap/Stance gap with a non-numeric side | Unambiguous; distinct from `#N/A` (malformed) and from empty (nothing). Same token everywhere "not applicable" means the same thing. | Two similar-looking tokens (`NA` vs `#N/A`) mean opposite things — has to be written down. |
| **B. Empty cell** | Tidy. | Collides with malformed. |
| **C. `0`** | Numeric column stays numeric. | Averageable; and `0` is not a level. |

### My recommendation

**A.** And the loader treats `NA`, `#N/A` and empty as three different things, by name.

### Your answer

: A

<!-- -->


---

## Q9 — Numbers or labels?

### What this is

Forms exports label text — `Often`, `Doer, spot-checked`, `Use it regularly`. The sheet converts labels to numbers to score them (#10 made lookup tables its first step). Does the CSV carry the numbers, the labels, or both?

### Why it matters

The dashboard needs numbers to compute and labels to render; it can own the label tables (they are short and fixed — five scales) or read them from the file. Labels in the file are readable by eye but are a parsing liability: `Doer, spot-checked` contains a comma, so every such cell is quoted, and a typo in one lookup table produces a label the dashboard doesn't recognise. Numbers are unambiguous and match the Rubric's "level 3" vocabulary; the only cost is that the raw CSV is unreadable without the key.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Numbers everywhere** — items 1–5, levels 1–6, tools 1–4, safeguards 0/1; the dashboard and the Rubric own the label tables | One representation; no quoting; the Rubric already speaks in levels. | The CSV needs the Rubric beside it to be read by eye. |
| **B. Labels everywhere** | Human-readable file. | Quoting, spelling drift, the dashboard reverse-maps everything; scores are numbers anyway so the file is mixed regardless. |
| **C. Both** — number column plus label column per measure | Readable and computable. | Doubles the width/rows for no computational gain; two things that can disagree. |

### My recommendation

**A.**

### Your answer

: A

<!-- -->


---

## Anything else — round 2

<!-- Free space. If long stands, this is where to say what else will read the file. -->


---
# Round 3 — the contract itself: names, order, encoding, and where the file lives

**Read-back of round 2:** Q5 **B — wide** (one row per Respondent). Q6 **A** — full precision, General format, dashboard rounds for display. Q7 **A** — `#N/A` in affected cells plus a `malformed` flag naming the blank items. Q8 **A** — literal `NA` for "I don't do this work" and for any Coverage gap with a non-numeric side. Q9 **A** — numbers everywhere; the dashboard and Rubric own the label tables.

With shape and value rules fixed, what is left is the header row — which under wide *is* the contract — plus three file-level rules. This should be the last round.

---

## Q10 — File-level columns

### What this is

The columns that describe the row rather than an answer: who, when, and two pieces of housekeeping the dashboard needs.

### Why it matters

- **`respondent`** — the join key. Forms' built-in *Name* column (#10). Display name, as Forms records it.
- **`completed`** — Forms' *Completion time*, as an ISO date (`2026-09-14`). Cheap provenance: which run this row came from, and whether someone answered before or after a team conversation. Not used by any prototype view, but it is the only timestamp we will ever have.
- **`roster_n`** — the team size, so "5 of 9 submitted" is on the face of the result (#9 §2.5). The CSV cannot infer it from its own rows; it is one cell in the sheet, repeated per row.
- **`schema`** — a version number (`1`) so the dashboard refuses a file it doesn't understand instead of rendering it wrongly. The pilot *will* change something.
- **Email** — Forms records it; nothing downstream needs it; the file travels. Excluded.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. All four: `schema`, `respondent`, `completed`, `roster_n`** | Self-describing file; the dashboard prompts for nothing. | Two columns (`schema`, `roster_n`) hold the same value on every row — mildly odd, entirely harmless. |
| **B. `respondent` only; dashboard asks for roster size; no version** | Minimal. | A prompt on every load; a schema change after the pilot fails silently. |
| **C. A, plus `email`** | Joinable to the org directory. | A file with names *and* emails is a worse thing to leak; nothing uses it. |

### My recommendation

**A.**

### Your answer

: A

<!-- -->


---

## Q11 — Header grammar

### What this is

The naming rule every one of the ~270 columns follows. The dashboard resolves columns by header text (never position), so the header row is the contract and it has to be systematic enough that a reader — or a formula — can predict a name without looking it up.

### Why it matters

Three candidate grammars, illustrated on the same four columns (Trust score for the team stance, Sofia's current Involvement level on Security review, her Test-suite safeguard in six months, and her raw answer to item C3):

| Grammar | Example headers |
|---|---|
| **Full words, dot-separated: `family.name.pass`** | `dimension.trust.future-team` · `area.security-review.current` · `safeguard.tests.future-personal` · `item.C3` |
| **Short codes** | `trust.ft` · `a14.cur` · `sg.fp.3` · `C3` |
| **Human headers** | `Trust — team should` · `Security review & threat modeling — today` · `Test suite passes — 6 months (me)` · `C3` |

Full words cost nothing (width is free) and every segment is a word from `CONTEXT.md`: `dimension`, `area`, `item`, `probe`, `edge`, `safeguard`, `lever`, `learn`, `gap`, `flag`, `context`; passes `current` / `future-personal` / `future-team`. Short codes are what the prototype used internally and what a formula author would reach for, but they need a key to read. Human headers are what Forms does — and #10 found that painful: spaces, dashes, commas, quoting, and text that someone will "tidy" in the sheet and break the join.

The **pass** vocabulary is the one place the grammar meets the glossary directly. `CONTEXT.md` says *Current score*, *Future score*, *Personal stance*, *Team stance*. `current` / `future-personal` / `future-team` reads those terms straight off; the ticket's `section + stance` split into two words would need two segments per column for the same information.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. `family.name.pass`, lowercase, full words, hyphens inside a segment, dots between** | Predictable; readable without a key; glossary words; safe in every CSV tool; a formula can build a header by concatenation. | Long headers (`dimension.guardrails.future-personal` is 36 characters). |
| **B. Short codes** | Compact; matches the prototype's internal names. | Needs a key; `a14` tells nobody anything; the number is an ordering, which is exactly what #10 said never to rely on. |
| **C. Human headers** | Readable in Excel. | Fragile to edit, quoting everywhere, no grammar to predict from. |

### My recommendation

**A.**

### Your answer

: A

<!-- -->


---

## Q12 — The key vocabulary

### What this is

The `name` segment of every header: what a Dimension, an area, a safeguard, a tool and an item are *called* in the file.

### Why it matters

Under Q11-A every key is a word, so the words have to be fixed once and never re-derived. Two choices inside this.

**Slugs or numbers for areas and safeguards?** Areas have a row number in `survey/coverage-grid.md` (1–19) and safeguards a position (1–7). Numbers are short but they are *orderings* — reorder the grid for readability and every `area.14.*` column silently means something else. Slugs (`security-review`, `tests`) survive reordering and are readable.

**Which slugs?** Derived from the glossary term, shortest unambiguous form, fixed in a key table inside the spec:

| Family | Keys |
|---|---|
| `dimension` / `gap` | `comfort` `trust` `fluency` `guardrails` `concern` `autonomy` `craft-values` |
| `area` / `area-gap` | `requirements` `architecture` `production-code` `tests` `code-review` `debugging` `documentation` `refactoring` `ci-cd` `infrastructure` `incident-response` `monitoring` `data-migrations` `security-review` `dependency-upgrades` `estimates` `stakeholder-comms` `learning` `meeting-notes` |
| `safeguard` / `lever` / `learn` | `read-myself` `another-person` `tests` `rollback` `schema-check` `small-blast-radius` `security-scan` |
| `context` | `copilot` `copilot-studio` `m365-copilot` `azure-ai-foundry` `other-tool` |
| `item` / `probe` | the bank IDs as they are: `C1` … `V3`, `FC1` … `FV3`, `P1` … `P5` |
| `flag` | `malformed` `inconsistent-current` `inconsistent-future-personal` `inconsistent-future-team` `hold` |
| `edge` | `P1` … `P5` (the probe it came from) |

Note `tests` appears as both an area and a safeguard — harmless, because the family segment disambiguates (`area.tests.current` vs `safeguard.tests.current`), but worth seeing.

Item IDs are the one place the file keeps a code rather than a word: the banks *are* the key, and #10 found item text is the database key in Forms — the ID is the stable name for it.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Slugs as tabled above, fixed in the spec's key table** | Readable, reorder-proof, one place to look up. | Slugs are a second naming of things `CONTEXT.md` names in prose — the key table is a glossary appendix that has to stay in step. |
| **B. Numbers for areas and safeguards (`area.14`, `safeguard.3`)** | Short; matches the grid's row numbers. | Ordering as identity; opaque. |
| **C. Full names as keys (`area.security-review-and-threat-modeling`)** | Nothing to look up. | 50-character headers; ampersands and slashes to sanitise. |

### My recommendation

**A.** Read the slug table above critically — it's the one thing on this ticket that's a *list*, and every entry is a name you'll see for the life of the survey.

### Your answer

: A

<!-- Any slug you'd rename? -->


---

## Q13 — Column order

### What this is

Whether the spec fixes the order of the ~270 columns, and whether the dashboard depends on it.

### Why it matters

#10's rule for the Forms export — resolve by header, never position — carries straight over: the dashboard must not care about order. But a *documented* order still helps humans: the sheet author lays out families in a predictable sequence, and someone opening the CSV finds identity first, scores before raw items, flags last.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Documented family order; the loader ignores it** — `schema, respondent, completed, roster_n` · `context` · `dimension` · `gap` · `area` · `area-gap` · `edge` · `safeguard` · `lever` · `learn` · `flag` · `item` · `probe` | Predictable file; nothing breaks if a column moves. | None of note. |
| **B. Order is part of the contract; the loader checks it** | Catches a mangled file early. | Rejects a file that is merely re-ordered — the thing #10 said Forms itself does. |
| **C. No documented order** | Nothing to maintain. | Every export looks different; harder to eyeball. |

### My recommendation

**A.** Scored things first, raw things last: the file reads top-down as "who → context → results → the evidence".

### Your answer

: A

<!-- -->


---

## Q14 — Encoding and delimiter

### What this is

The save format the sheet's instructions mandate, and what the loader tolerates.

### Why it matters

Excel offers several "CSV" save types. **"CSV UTF-8 (comma delimited)"** writes UTF-8 with a byte-order mark; plain "CSV (comma delimited)" writes the Windows code page — which turns an em-dash or a name like *Marchetti* with any accent into mojibake (the same failure that hit the map issue on this project). And on a Windows locale whose list separator is `;`, Excel writes semicolons whatever the save type says. Names in this file are exactly the kind of text that carries accents.

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. Mandate "CSV UTF-8 (comma delimited)" in #15's instructions, *and* the loader strips a BOM and sniffs `,` vs `;` from the header row** | Correct by instruction, tolerant by code. A `;` file from a European locale still loads. | The loader has ~5 lines of sniffing. |
| **B. Mandate only** | Simplest loader. | One wrong click in Save As produces a file the dashboard can't read, with no useful error. |
| **C. Sniff only** | No instruction needed. | Code-page files still mangle names; sniffing can't fix encoding. |

### My recommendation

**A.**

### Your answer

: A

<!-- -->


---

## Q15 — Where the file lives, and a sample

### What this is

This repository is **public**. A scored CSV is a table of named colleagues' answers about trust, concern and job impact. It must never be committed. But #16 needs a file to build against before the pilot exists, and the spec needs an example to make the header grammar concrete.

### Why it matters

Two files, two rules:

- **A sample CSV** in the repo — generated from the prototype's seven fake personas (`dashboard/prototype-slices.html` already scores them with the real rules), so it exercises every family: a `NA`, a mixed N/A pair, an inconsistency flag, Edge markers in all three states, a Lever, a principle hold. It is the fixture #16 develops against and the worked example the spec points at. Named `scoring/scored-sample.csv`, with fake names that could not be mistaken for the team.
- **Real exports** — never in the repo. A `.gitignore` rule (the repo currently has no `.gitignore`) that ignores `scoring/*.csv` and re-includes the sample by name. The instructions on #15 say where real exports go (a local folder, or the team's SharePoint — not this repo).

### Options

| Option | Pros | Cons |
|---|---|---|
| **A. `scoring/scored-sample.csv` from the fake personas + `.gitignore` for real exports** | A fixture and a worked example for free; the leak is prevented by the repo, not by remembering. | The sample must be regenerated if the schema changes — a script or a formula path from the prototype's data. |
| **B. Sample only, no ignore rule** | Less setup. | One `git add .` after the pilot publishes seven colleagues' Concern scores. |
| **C. No sample; #16 waits for the pilot** | Nothing fake in the repo. | #16 can't start, and the spec has no example. |

### My recommendation

**A.** I'd generate the sample from the prototype's personas as part of resolving this ticket, so the spec and its example land together.

### Your answer

: A

<!-- -->


---

## Anything else — round 3

<!-- Last call. Slug renames, a column you know a future view will need, anything the pilot should be able to change without breaking the file. -->


---
