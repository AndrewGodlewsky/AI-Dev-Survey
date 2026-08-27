---
status: accepted
date: 2026-08-27
---

# Replace the non-leading rule with the Framing rule

v1's survey carried an absolute **non-leading rule**: never ask *"what would have to be true for
you to accept X"*, because it presupposes X is a destination. It was the reason Conditional
items became Safeguard items and Levers are derived rather than asked. The author's own pilot
found the forward-looking block returned the present — asking the same items twice in a future
tense gets the same answers — and asked for scenario-style items instead (*"if this were true,
how would you feel?"*), which the old shape-ban could neither permit nor safely check.

**Decision:** v2 replaces the shape-ban with a rule that names the harm — **no implied
destination**, symmetric, applied to everything the Respondent reads — plus a closed catalogue
of five item forms and an ordered five-check test. The rule lives in
[`survey/item-framing-rule.md`](../../survey/item-framing-rule.md); it is binding and is not
re-litigated per item. Grilling record:
[`docs/grilling/issue-22-item-framing-rule.md`](../grilling/issue-22-item-framing-rule.md)
([#22](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/22)).

## Considered options

- **Overturn the rule outright** and allow "what would it take" items. Rejected: that framing tells the Respondent where the finish line is and that they are behind it, on a survey their team reads by name.
- **No advocacy** as the principle (asking is not endorsing). Rejected as the loophole, not the rule — the author's own "what AI would have to do for them to use it more" advocates nothing and still points.
- **No socially costly answer** as the principle. Rejected: it would ban the Concern and Craft probes, which are meant to be costly to endorse. It is a consequence of the chosen rule, not its headline.
- **A directional rule** (ban only pro-AI framing). Rejected: it cannot be applied without first arguing which way an item leans, which is per-item litigation.

## Consequences

- **Threshold items stay banned**, so Levers remain derived by subtraction; if the future-personal Safeguard asking is cut, Levers go with it.
- **Abstract Value items are legal only in the team section.** The forward personal block is concrete-only: Scenario and Direction items.
- **Ordinal scales are instruments, not option lists** — the frozen Coverage grid's 1–6 ladder passes; the check for a scale is that both end labels are equally sayable.
- **The rule binds the bank**: every Scenario/Direction block carries at least one less-AI-than-today item.
- v1's *Stance gap* and *norm gap* were already dead on other grounds; this ADR does not revive them.
