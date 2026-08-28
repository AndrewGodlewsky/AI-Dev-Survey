# Grilling — Issue #32: Direction item bank

**Ticket:** [Direction item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32)
**Map:** [Map v2: Survey overhaul & local dashboard app](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/21)
**Round:** 1 of ~2 — seven questions *(round 2 applies your answers to the spec files)*
**How to use:** the draft bank is [`survey/direction-items.md`](../../survey/direction-items.md) — read that first, it is the thing being reacted to. Then answer inline under each `### Your answer` heading below. Free text is fine; you don't have to pick a listed option. Tell me when it's ready and I'll read it back.

---

## What is already settled coming in

- **The allocation is fixed** by [Forward personal block](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24): Comfort 2 · Trust 2 · Fluency 2 · Guardrails 5 (one per facet) · Concern 5 (one per risk) · Autonomy 2 · Craft 2 = **20**. *"One fewer item anywhere breaks Gap on a bundle."* Not up for renegotiation here.
- **Single row, Desirability scale, no *six months* in any item**, horizon named once in the section description. Stance is dead.
- **≥1 reverse-keyed item per Dimension.** All seven have one: D-C2, D-T2, D-F2, D-G5, D-N4, D-A2, D-V2.
- **The Framing rule is not re-litigated per item.** A draft is one of the five forms and passes the five-check test, or it isn't an item. Every item in the bank passed; **this record only shows the working for the calls I was unsure about.** If a question below feels like it's arguing an item rather than deciding a trade, say so and I'll drop it.
- **No Value items** in this block — concrete only.
- **The balance floor is met**: seven of twenty describe less AI or a held status quo.
- **Every statement in the form must be unique**, and no Direction item may be a Current-state item's sentence in another tense. Five drafts were rewritten for collision (table in the bank); those five are **not** questions here — they were mechanical fixes.

## What this round holds back

- **Block structure, item order, probe placement** — [Assemble the v2 survey document](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/29)'s, once the bank exists.
- **The scoring arithmetic** for a 2-item Direction mean against a 3-item Current mean — [Scoring rules v2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/28). Q1–Q3 below tell it *how soft* each Gap is; #28 decides what to do about it.
- **The Team section's items** — [Team item bank](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/31), a sibling ticket. Q5 touches the boundary between the two sections but does not draft anything on the team side.
- **Applying the amendments** to `probe-items.md` and `safeguard-items.md` — round 2, once Q6 and Q7 are answered.

---

## Q1 — Trust: should the reverse item stay off "line by line"?

### What this is

Trust has **two** scored slots. The obvious reverse-keyed item is v1's FT2 — *"I read AI-written code line by line before it is used."* But the Trust **probe** (P2) is *"I merge AI-written code I have not read line by line, as long as the tests pass"*, and in v2 both sit in **one 25-row block on one scale**, a few rows apart.

I moved the scored item onto different words:

> **D-T2** — *I check AI's work against the source — the docs, the code, the data — before I act on it.*

### Why it matters

This is the exact failure [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) caught in v1 between Guardrails FG3 and the Concern probe: two near-identical sentences, rows apart, on the same scale — a Respondent notices, and one of the two slots is wasted. With only two Trust slots, wasting one is worse than it was in v1, where Trust had three.

The cost: D-T2 is *verification before acting* rather than *line-by-line reading*, so Trust's Gap against T2 is facet-matched rather than word-matched — softer, like the Fluency and Craft Gaps v1 already flagged.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep D-T2 as source-checking** *(drafted)* | Probe keeps its ground; both slots earn their place; covers a Trust behaviour the bank otherwise misses (acting on answers, not just merging code) | Trust's Gap is softer; T2's exact behaviour has no forward twin |
| Use FT2's wording, reword the probe instead | Word-matched Gap on Trust | The probe *is* the extreme version of that sentence — there is nowhere else at Trust's high pole to move it, and it's the most-used probe in v1's design |
| Use FT2's wording and accept the collision | Simplest; v1 shipped exactly this pair | The pilot already found the forward block repetitive; this is a visible instance of why |
| Drop the Trust probe entirely | Frees the sentence | Probes are five, one pole each, decided in [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8); dropping one reopens that ticket |

### My recommendation

**Keep D-T2 as drafted.** The probe is the sharper instrument on that exact sentence — it's the one that produces a name in the room — and a scored item can move without losing the Dimension. Not a close call.

### Your answer:

---

## Q2 — Fluency: are two adjacent items one item too many?

### What this is

Fluency's two slots, as drafted:

> **D-F1** — *I want to point AI at the right files and examples before I ask it anything.* (per-task context)
> **D-F2** (R) — *I want to use AI tools as they come, without configuring or tuning them.* (tool setup)

They are different acts — what you feed it each time, against whether you tune the tool at all — but they sit on one axis: **how much effort you put in around the tool.** Someone high on one is usually high on the other.

### Why it matters

Fluency's Current bank has three items (outcome, context habit, failure-mode confidence). Two of those three don't survive onto a Desirability scale: F1's *"get a usable result in a try or two"* floors out as a want (nobody wants more tries), and F3's *"I'm not sure what to change"* floors out for the reason v1 documented. That leaves the context/setup axis carrying **both** Fluency slots.

If the two items never diverge, Fluency's Direction score is effectively one item doubled, and its Gap moves a full point when one answer moves — the thing the spec warns about (*"±0.5 on a two-item Dimension is one item moving a point"*).

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep both as drafted** | Two genuinely different acts; the reverse-key requirement is met naturally; pilot data will show whether they diverge | Possible redundancy; Fluency reads thin |
| Replace D-F1 with a **tool-breadth** item — *"I want to work with agents and custom rules, not just chat and autocomplete"* | Clearly a second axis; concrete; names artifacts | Brushes Autonomy D-A1 (agents), and "custom rules" is configuring — the overlap moves rather than goes |
| Replace D-F1 with a **failure-mode** item — *"When an AI tool gives me the wrong thing, I want to know what to change rather than try again"* | Recovers F3's facet, which currently has no forward twin at all | Half-confession shape; risks the same floor F3 hit |
| Accept the redundancy and note Fluency as the weakest Dimension in the one-pager | Honest; costs nothing to build | Leaves a known-thin score in a scored instrument |

### My recommendation

**Keep both, and flag Fluency to the pilot as the Dimension most likely to need a third item.** The tool-breadth alternative trades one overlap for another and picks a fight with Autonomy; the failure-mode alternative re-runs the floor v1 already hit. This is the closest call in the bank — if you have a Fluency behaviour in mind that neither item catches, that's the better third option than any of mine.

### Your answer:

---

## Q3 — Autonomy: the reverse item changed facet. Accept the softer Gap?

### What this is

Current A2 is *"How often do you approve an agent's steps as it goes, rather than letting it run on?"* — the leash. The drafted forward reverse-key is:

> **D-A2** (R) — *AI suggests and explains; I make the actual edits myself.*

That is the **Advisor** position (Involvement level 2), not step-approval. I moved it because A2's own sentence, put forward, lands next to the Autonomy probe (*"let an agent work unsupervised for an hour and only look at the final result"*) on the same supervision axis — the Q1 problem again, in a Dimension that also has only two slots.

### Why it matters

Autonomy is the Dimension the dashboard's headline reading leans on. A softer Gap there costs more than a softer Gap on Fluency. The trade: D-A1 (*agents change files across my project*) and D-A2 (*AI suggests, I edit*) are two clean anchors on **how far AI's hand reaches**, which is arguably the Dimension's real axis and reads better than two points on supervision.

### Options

| Option | Pros | Cons |
|---|---|---|
| **D-A2 as the Advisor position** *(drafted)* | Two clean anchors on one axis; probe keeps duration to itself; matches the Involvement scale's own vocabulary | Autonomy's Gap is facet-matched, not word-matched — one more soft Gap |
| D-A2 as step-approval, word-matched to A2 | Hardest Gap on the Dimension that most needs one | Sits on the probe's axis; two of three Autonomy rows then say "supervision" |
| Word-match A2 **and** move the probe to a different Autonomy pole | Both hard | There isn't an obvious second high pole for Autonomy that isn't "unsupervised for a long time" |

### My recommendation

**Keep D-A2 as drafted.** Three of the seven Gaps are already facet-matched; a fourth is not the thing that breaks the instrument, and #24 already ruled every Gap is the softer kind now. Two clean anchors beat one hard Gap and a wasted row. Moderately close.

### Your answer:

---

## Q4 — Guardrails: D-G1 and D-G5 are near-inverses. Live with it?

### What this is

> **D-G1** — *Anything AI helped write goes through an extra pair of eyes and an extra test before it ships.*
> **D-G5** (R) — *AI-assisted work moves through the same pipeline as everything else, with nothing added for it.*

Answering *Definitely* to one implies *Definitely not* to the other. This is inherited: Current G1 and G6 have the same shape, and [#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18) was already told to *"watch G1/G6 for whether the reverse-key is reading as a trick."*

### Why it matters

It cannot be fixed by dropping one — both are **named facets** (*review + testing*, *the "nothing extra" pole*) and the Gap needs all five. So the only lever is wording: how far apart can the two sentences be pushed while both still name their facet?

A Respondent who spots the pair may answer the second from the first rather than from scratch, which is a soft form of the straight-lining [#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20) exists to catch. It also means Guardrails' reverse-key does less attention-check work than the other six.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep as drafted, separated by wording** *(review-and-test vs pipeline)* | Both facets named; different nouns; matches the frozen Current pair, so the Gap subtracts like for like | Still logical inverses; the pair is visible if the two land near each other |
| Reword D-G5 onto **cost** — *"the extra process around AI-assisted work isn't worth what it buys"* | Genuinely different sentence; a real and separate position | Drifts from G6's facet (*nothing extra applies*) toward Concern; Gap gets softer on a bundle facet, which #24 said not to do |
| Keep both and require #29 to **separate them in the form** | Zero wording cost; mitigation where the problem actually shows | Depends on block structure not yet decided; a mitigation, not a fix |
| Reopen the facet list and merge the two | Removes the problem at the root | Reopens [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24)'s allocation and breaks Guardrails' Gap |

### My recommendation

**Keep as drafted, and hand #29 an explicit instruction to put distance between D-G1 and D-G5.** The pair is structural — the frozen bank has it too, so removing it forward would make the Gap subtract different things. Wording separation plus placement separation is the honest ceiling here.

### Your answer:

---

## Q5 — Voice: two items say "our", in a personal section

### What this is

The Direction section is the **personal** block; the Team section now owns *"the team should"*. But two Guardrails items are unavoidably collective:

> **D-G4** — *Our AI rules live in the tooling — lint, CI, hooks — not in people's heads.*
> **D-G5** (R) — *AI-assisted work moves through the same pipeline as everything else, with nothing added for it.*

Enforcement and pipeline are properties of a shared environment; you cannot have a personal CI policy. Their Current twins (G5, G6) are voiced the same way, in the frozen bank.

Formally these are **Scenario items** — a world you're asked whether you'd want to work in — not Direction items proposing a norm, so they don't trespass. But a Respondent doesn't read labels.

### Why it matters

The single biggest structural change in v2 is that the personal and team questions became **different questions** instead of two rows of one. If the personal section still contains sentences about what the team does, the pilot's *"re-answering the same questions"* complaint can come back through a side door — especially since the Team section will have its own Transparency and Verification items in the same neighbourhood.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Keep both as worlds** *(drafted)* | Word-matched to the frozen G5/G6, so Guardrails' Gap is the hardest in the bank; legal under the rule | Two "our" sentences in a "me" section; possible echo against the Team section |
| Re-voice to first person — *"I want the AI rules I work under to be enforced by tooling"* | Consistent voice throughout the section | Contrived (you don't choose your CI alone); softens the Gap on two of Guardrails' five facets |
| Keep them, and add a line to the section description — *"a few of these describe how the team works; answer them as the world you'd want to work in"* | Cheap; removes the ambiguity for the Respondent explicitly | One more sentence of copy, which must itself pass the Framing rule |
| Move enforcement to the Team section entirely | Cleanest voice split | Breaks Guardrails' five-facet Gap; reopens [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) |

### My recommendation

**Keep both, and add the one-line clarification to the section description** (option 3 on top of option 1). The Gap on Guardrails is the one place the bank is fully word-matched and that's worth protecting; the ambiguity is real but it's a copy problem, and copy is cheap. I'd want the exact sentence checked against the Framing rule in round 2 before it lands.

### Your answer:

---

## Q6 — The Safeguard list: my ordering, and a change to the Current-state section

### What this is

Two things, both about the eight-option symmetric list. They travel together because both are changes to the frozen-adjacent Current-state Safeguard item.

**(a) Order.** `direction-section.md` lists the three reading positions first, then the five checks. That reads as an escalation from human to automated — a **ramp**, which option-list mechanic 2 bans. I interleaved them so reading positions land at 2, 4 and 6 and neither group is a bloc.

**(b) Asking 1's stem.** The Current-state section currently asks *"Which of these, if any, do you accept today **instead of reading AI's output yourself**?"* — the leaning framing [#24](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/24) removed. The list is replaced regardless; the stem has to change with it, or the question contradicts its own options. Drafted: *"For AI-written output, which of these count, for you, as enough today?"*

### Why it matters

(a) is the kind of thing the Framing rule exists to catch and nobody notices in a spec — a list order is copy the Respondent reads.

(b) is a **scope call**. The Current-state section is frozen, and this touches it. The freeze covers *"the 26 scored items"* and the Coverage grid's today pass; Safeguard item 1 is neither. But it sits in that section, and the map is emphatic about what's frozen — so I'd rather you rule on it than assume.

### Options

| Option | Pros | Cons |
|---|---|---|
| **Interleave, and rewrite asking 1's stem** *(drafted)* | Both halves consistent with the rule; the three askings read as three questions; Levers and Holds subtract identical lists | Touches the Current-state section |
| Interleave, keep asking 1's old stem | Leaves the frozen section alone | The stem says *instead of reading it yourself* while the options offer three ways of reading — self-contradictory |
| Keep the spec's order, rewrite the stem | Order stays as decided in #24 | The order is a ramp; the rule bans it |
| Neither — leave the Current-state asking entirely alone, new list in the Direction section only | Maximum respect for the freeze | **Breaks Levers and Holds.** They are subtractions; different lists on the two sides means nothing to subtract |

### My recommendation

**As drafted.** Option 4 is disqualified — it kills the two signals the section exists to produce. Given that, asking 1 has to change, and once it's changing, the stem should match its options. The freeze protects the 26 scored items; this isn't one. I'd still like the ruling on record.

### Your answer:

---

## Q7 — The Concern probe, amended a second time

### What this is

`probe-items.md` P4 reads *"…**slow down** how fast I adopt AI, because the risks outweigh what I'd gain."* *Slow down* is a comparative against the Respondent's present pace — squarely inside the Framing rule's ramp ban (*"more than today, go as far as, beyond what I do now, and any comparative against the Respondent's present position"*).

Drafted replacement:

> **P4** — *I hold back on AI, because the risks outweigh what I'd gain.*

This is the **second** amendment to that probe. [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) already moved it off *"work AI is not allowed to touch"* because it collided with Guardrails FG3.

### Why it matters

Two rewrites of one sentence is a signal, not a coincidence: Concern's high pole is hard to state concretely without either naming a no-go area (Guardrails' ground) or naming a pace (a comparative). If *hold back* doesn't sit right either, the honest answer might be that Concern's probe wants a different pole rather than a third rewording.

The mechanics are unaffected — still five probes, one pole each, *Definitely* is still the edge — so this is a wording amendment to a closed ticket, not a reopening.

### Options

| Option | Pros | Cons |
|---|---|---|
| ***I hold back on AI, because the risks outweigh what I'd gain*** *(drafted)* | No comparative; states a standing position; same pole; smallest change | *Hold back* still faintly implies a thing being held back from |
| *I'd rather carry the risks of moving slowly on AI than the risks of moving fast on it* | Both poles inside the sentence, like D-G4; genuinely symmetric | Long, and needs thinking through — the rule says a gut-reaction item has already failed |
| Move the pole — *"I want a named person accountable for every AI-written change that reaches production"* | Concrete, no comparative, a real Concern edge; nothing else in the bank occupies it | Reads close to the Team section's Transparency facet; a third rewrite of a closed decision |
| Leave P4 as-is and accept the ramp word | Zero churn | The rule is binding and *slow down* is explicitly the banned shape |

### My recommendation

**The drafted wording.** It is the smallest change that removes the violation, and the residual implication in *hold back* is carried by the scale, not the sentence — which is what the rule permits. Option 3 is the one worth a look if you think Concern's high pole has been in the wrong place both times.

### Your answer:

---

## Anything else

Anything in the bank that reads wrong, sounds unlike this team, or would make you hesitate to answer honestly on a survey your colleagues and manager will read — including items I didn't flag. The five-check test catches structure; it doesn't catch an item that's simply a bad question about *this* team's work.

Worth a specific look:

- **D-C1** carries both frequency and stakes in one sentence (*"most of the code I write, including the code that ships to production"*). Two ideas, one row.
- **D-N2 and D-G1** are neighbours — a security gate against general added rigour.
- **D-V1** (*"leave code the next person can work on without asking me"*) is the one Craft item, and Craft is deliberately not AI-specific. Does it still read as a craft value rather than a documentation habit?

### Your answer:

