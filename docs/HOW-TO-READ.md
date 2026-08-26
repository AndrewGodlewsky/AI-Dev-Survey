# How to read the results

One page for everyone who took the survey. Written in wayfinder ticket [#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17); the
rules it summarises live in `rubric/RUBRIC.md` (§7 especially) and `scoring/scoring-rules.md`. **Nothing here ranks anyone.** Every number is
a position on a scale that runs in its natural direction; none is a grade.

## 1. What you are looking at

- **`dashboard/index.html`**, opened from disk, with the scored CSV loaded by picker or drag-drop. Left: **Team overview**, then every topic
  (7 Dimensions + 19 Development areas) **ordered by how much we disagree today**. Right: the selected topic.
- **Two views**, toggled in the filter row. **Internal (named)** is for everyone who took the survey — every person's value is plotted and named.
  **Exported team view** carries no names: counts per level, means, ranges, medians. The **Team overview** page is *always* the exported form;
  it is the only thing that goes to the manager, as **Print / save as PDF** (button in its banner). **The CSV itself never travels upward.**
- **The Context lens** (tool × usage state) filters to the people who match. It changes `n` on every page — read every team number as
  *"over n of the roster"*, which each one prints beside itself.

## 2. What the numbers are

| Rule | Read it as |
|---|---|
| **The decimal is the score; the integer is a landmark.** | "Trust 3.4 — closest to level 3: *trusts AI output on familiar, well-specified work…*". The level text is a translation; the number is the finding. Never say "Level 3". |
| **A Gap of 0.3 is real.** | Gap = *6 months (me)* − *today*. On a three-facet Dimension, 0.3 is one facet moving a full point. Positive = wants more of it; negative = wants to pull back. |
| **Fluency and Craft values Gaps are softer.** | Their future items match the current ones by facet, not word for word. Quote them to the nearest half point, not the decimal. The dashboard marks them *softer*. |
| **Stance gap** = *team should* − *6 months (me)* | Negative = **"I'd go further than the team should."** Positive = **"the team should go further than I would."** Both ends are the same person's own answers, so it is a real quantity. Within ±0.3 counts as aligned. |
| **Guardrails high ≠ responsible. Concern high ≠ negative.** | Both are positions. Concern's five facets are the diagnosis; the mean is only the summary. |
| **Team = mean + range + every value. No standard deviation.** | At 5–9 people a deviation looks authoritative and means little. Range (max − min) is only there to order topics by disagreement. |
| **Coverage is a profile, not a score.** | Per area: how many people at each Involvement level (1 None → 6 System-verified). The outlined cell is the median (lower middle at even `n`) — the only number Coverage gets. **Never average across areas.** Gap is the median of each person's own move, in levels. N/A ("I don't do this work") is excluded but counted; an N/A on one side and a level on the other is a staffing signal, not an adoption signal, and has no Gap. |
| **`#N/A` / "malformed" is a defect, not a result.** | Someone left a required item blank. That Dimension is excluded for them with a visible flag — never averaged around. Recovery is a conversation, not a formula. |

## 3. The Slices

| Slice | Shows | Look for |
|---|---|---|
| **Team overview** | Per Dimension: how many at each level for *today / 6 months (me) / team should*, the three means on one axis, Gap, norm gap, stance split. Coverage by area group. Draft norms. Edge-marker counts. | Where today's mean, the personal target and the team-stance target sit relative to each other. Where the level counts spread across three or more columns. |
| **A Dimension** (Layered view) | Every person's *today* and *6 months* joined by a connector, over the team mean and the team-stance target; histogram; who is where. | Long connectors; connectors pointing opposite ways; people far from the mean line; the histogram splitting into two clumps. Trust and Autonomy show the Safeguards beneath — read them together. |
| **A Development area** | People placed on the 1–6 Involvement scale per pass; the all-areas heatmap. | Where the median moves; anyone at 6 on a ◆ high-stakes area; rows where many say N/A. |
| **People** | One person: all seven Dimensions against the team mean, their Coverage strip, Safeguards, Edge markers. Internal only. | Their own shape — not their rank. |
| **Stance gaps & probes** | Per Dimension, who would go further than the team should and who thinks the team should go further than they would; the probe table. | A Dimension where the stance split is not "mostly aligned". |
| **Safeguards** | What people accept instead of reading AI's output themselves — today, in 6 months, and as a team norm — plus Levers, holds and learning interest. | Anything at least half the team says the team should accept: that is a **draft six-month norm** you can write down. |
| **Craft × Comfort** | One dot per person on two axes. | High craft + high comfort is a different team from high craft + low comfort. A lens, not a metric. |

## 4. When you see it, ask yourselves

| Signal | What it means | The question |
|---|---|---|
| **A large personal Gap** on a Dimension (team Gap well beyond ±0.5, or most connectors long) | The team wants to move — up or down. The direction matters more than the size. | *What is the one thing that would let us close this in six months — and does the Safeguards page already name it (a Lever)?* |
| **A large spread** (a wide range today; level counts in three or more columns) | We do not agree where we are. That is a finding, not noise — at this `n` the dashboard shows every point so you can see *who* disagrees. | *Is the disagreement about the facts of our work, or about the value we place on it? Is it two clumps, or one outlier? Talk to the ends, not the mean.* |
| **A Personal-vs-Team split** (many negative Stance gaps) | People would go further themselves than they think the team should. Usually: "I trust *my* judgement, not a norm." | *What would a team norm need to say for the people ahead of it to feel it is safe for everyone else?* |
| **The opposite split** (many positive Stance gaps) | People think the team should go further than they personally would. | *Who is expected to carry the norm, and do they want to? Is this a skills request in disguise — check learning interest.* |
| **A norm gap** far from the personal Gap | What the team thinks *the team should* do diverges from what its members *would* do. | *Are we drafting a norm nobody intends to live by?* |
| **Pole-probe agreement** (several markers on one probe) | A cluster at an edge — an accelerator (Trust, Autonomy, Craft values), a brake (Concern), or "fine without AI" (Comfort). *Both stances* = they'd do it and want the norm; *me only* = "I'd go, but we shouldn't"; *team only* = "the team should, but not me". | *Is the edge a place we want a norm to reach, a place we want a guardrail in front of, or just where a few people already work? Name it either way.* |
| **A level 6 on a ◆ high-stakes area** | Someone runs — or wants to run — AI end-to-end with only automated checks on Code review, CI/CD, IaC, Incident response, SQL/data migrations or Security review. Labelled with its pass: today and six months are different statements. | *Which checks would have to exist for that to be acceptable to the rest of us — and do they exist?* |
| **A principle hold** ("I'd read it myself" in six months) | The line does not move for this person. A real constraint on the plan, not an obstacle. | *Does the draft norm leave room for it?* |
| **An inconsistent Safeguard answer** or a **malformed** row | Not a result. Levers are not computed for that person; the Dimension reads `#N/A`. | *Go and ask them.* |

## 5. Two things to say out loud before sharing

- **Edge markers, holds and flags locate positions, never faults.** None of them enters a score.
- **The exported view is not anonymous.** At 5–9 people an unnamed distribution is partially re-identifiable by anyone who knows the team. It is
  stated, not engineered away; if that feels too close, drop the distributions from the export and send means and ranges only.
