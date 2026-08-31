# Probe items and Edge markers

**DRAFT for reaction** — wayfinder ticket [#8](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/8).
Grilling record: [`docs/grilling/issue-8-probe-items.md`](../docs/grilling/issue-8-probe-items.md).

A **Probe item** is a deliberately extreme, concrete statement placed at one pole of a
Dimension. It is a **marker, not a measurement**: it never enters a Dimension score.
Endorsing one raises an **Edge marker** against that named Respondent.

Probes replace the free-text questions the survey deliberately has none of. Their output
is not a number — it is a sentence somebody has to own in the room.

---

## The rules

1. **Never scored.** A probe answer does not enter any Dimension mean, current or future.
   It therefore also cannot be reverse-keyed — the "at least one reverse-keyed item per
   Dimension" requirement from [#2](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/2)
   falls entirely on the ordinary items.
2. **Five probes, one pole each** — the poles where an edge position is a real constraint
   on the six-month plan. Fluency and Guardrails carry none.
3. **Future-state section only**, so every probe is answered twice: *For me* and
   *For the team*.
4. **Same Desirability scale, same Likert block** as the ordinary items of that Dimension.
   A Respondent cannot tell a probe from its neighbours.
5. **Direction-normalised**: every probe is worded so that **"Definitely" is the edge**,
   including Comfort's low-pole probe. One threshold, no direction lookup anywhere.
6. **An Edge marker fires at 4 or 5**, tracked **separately per stance row**.
7. **Concrete scenario**: a named action with a named condition, drawn from work this team
   actually does. Never an abstract maximal statement ("I completely trust AI").

## The five probes

Wording is a draft for the Future-state item bank
([#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6)) to polish. The rules above
are the decision; these sentences are not.

> **v2 — the live probe wording is in [`direction-items.md`](direction-items.md).** The five
> probes are **re-tensed from forecasts to present-tense worlds** and asked on a **single row**
> (Stance is dead, so the *For the team* column below no longer exists), per
> [`direction-section.md`](direction-section.md) rule 7. Rules 1–7 above stand unchanged, except
> that rule 3 now reads *Direction section only* and rule 6's **per-stance tracking is gone** —
> an Edge marker is one per Respondent per probe. The table below is v1's record.

| Dimension | Pole | *For me* — "In six months, I would…" | *For the team* — "In six months, the team should…" |
|---|---|---|---|
| **Comfort** | low | …be happy working with no AI tooling at all, the way I worked before it existed. | …be fine going back to working with no AI tooling at all. |
| **Trust** | high | …merge AI-written code I had not read line by line, as long as the tests pass. | …merge AI-written code nobody has read line by line, as long as the tests pass. |
| **Autonomy** | high | …let an agent work unsupervised for an hour and only look at the final result. | …let agents work unsupervised for an hour and only review the final result. |
| **Concern** | high | …hold back on AI, because the risks outweigh what I'd gain. | …hold back on AI, because the risks outweigh what we'd gain. |
| **Craft values** | high | …expect to be able to explain every line of code that ships under my name. | …expect everyone to be able to explain every line that ships under their name. |

> **Amended by [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6), 2026-08-26 —
> the Concern probe only.** It originally read *"…want there to be work here that AI is not
> allowed to touch at all."* Once the Future-state bank was drafted, that sentence sat rows
> away from a **scored** Guardrails item (FG3, "…keep parts of our work where AI isn't used at
> all") on the same scale in the same block — near-identical wording, one of the two slots
> wasted, and a Respondent certain to notice. The probe moved to the risk-appetite pole
> instead, which is sharper Concern anyway. Every rule on this page stands unchanged: still
> five probes, one pole each, Concern still high.

> **Amended a second time by the item banks' joint resolution, 2026-08-30 — the Concern probe
> again** ([#32](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/32) Q7;
> [`issue-31-32-item-banks-resolution.md`](../docs/grilling/issue-31-32-item-banks-resolution.md)).
> The risk-appetite wording above read *"…**slow down** how fast I adopt AI"* — a **comparative
> against the Respondent's present pace**, which the [Framing rule](item-framing-rule.md) bans
> outright as ramp vocabulary. *Hold back* states the position without measuring it against
> today. Every rule on this page still stands: five probes, one pole each, Concern still high.
>
> Two rewrites of one sentence is a signal, not a coincidence — Concern's high pole is hard to
> state concretely without either naming a no-go area (Guardrails' ground) or naming a pace (a
> comparative). If the pilot finds *hold back* reads wrong too, the honest answer is that
> Concern's probe wants a **different pole** rather than a third rewording.

Note the shape of the set: four probes sit at the **high** pole and only Comfort sits low.
The team's current position *is* the low end, so a low-pole probe mostly measures "normal".
Comfort is the exception because refusing AI outright is both rare and genuinely blocking.

## Edge markers from the Coverage grid

The grid carries **no probe rows** — Involvement level **6 (System-verified)** already is a
probe, once per Development area, at zero cost. Selecting 6 raises an Edge marker, but only
on the areas where an undetected error is expensive or hard to reverse:

- Security review / threat modeling
- Incident response / on-call
- Code review
- SQL / data migrations
- Infrastructure-as-code
- CI/CD & build config

A 6 on any other area (Meeting notes, Documentation, …) is unremarkable and raises nothing.
Firing on all 19 rows would let the ordinary sixes drown the alarming ones.

## What this hands downstream

- **[#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6) Future-state item bank** — write the five probes to the rules above; carry the reverse-keying requirement on the ordinary items alone.
- **[#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5) Current-state item bank** — no probes. Nothing to do.
- **[#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) Scoring rules** — probe answers are excluded from every Dimension mean; the Edge marker is computed, not scored.
- **[#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) Scored CSV** — needs a non-scoring per-Respondent attribute alongside `score`, shared with whatever [#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19) lands on.
- **[#16](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/16) Dashboard** — renders three states per probe: *accelerator* (both rows), *"I'd go, but we shouldn't"* (personal only), *"the team should, but not me"* (team only).
- **[#17](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/17) How to read the results** — must say plainly that an Edge marker locates a position, it does not report a fault.
