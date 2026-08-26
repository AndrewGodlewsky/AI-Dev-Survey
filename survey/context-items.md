# Context items

Decided in wayfinder ticket [#7](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/7).
Grilling record: [`docs/grilling/issue-7-context-items.md`](../docs/grilling/issue-7-context-items.md).

**Context items are unscored.** They describe the Respondent and act as a lens for reading the scored results; they never feed a Dimension score, a Gap, or the Coverage profile.

There is exactly **one** Context item. It goes at the **start** of the survey, before the Current-state section, as a warm-up.

## The item

**Question text**

> Which of these AI tools do you use in your development work?

**Help text**

> This is about enablement, not compliance — we're mapping what the team actually reaches for so we know what to support. There is no wrong answer, including "never used".

**Type:** Microsoft Forms *Likert / matrix* question. **Required.** Every row has a valid answer (`Never used`), so requiring it forces nobody into a false statement.

### Columns (4 states, same for every row)

| # | Column header | Means |
|---|---|---|
| 1 | **Never used** | I have not used this. |
| 2 | **Tried it, not using it now** | I gave it a go and stopped. |
| 3 | **Use it occasionally** | I reach for it sometimes. |
| 4 | **Use it regularly** | It's part of how I work. |

`Tried it, not using it now` is the load-bearing column: it separates "no exposure" from "had exposure and walked away", which a plain multi-select cannot express.

### Rows (5)

| # | Row text |
|---|---|
| 1 | GitHub Copilot |
| 2 | Copilot Studio |
| 3 | Microsoft 365 Copilot |
| 4 | Azure AI Foundry |
| 5 | Another AI tool not on this list |

Row 5 is deliberately unnamed and has no free-text follow-up. It measures *whether* the sanctioned estate is the whole picture without asking anyone to name an unsanctioned tool under their own name in an openly-shared result.

## How it is used

Read as a **lens**, not a metric. Copilot and Azure AI Foundry are used for different work in different ways, so which tools a Respondent lives in plausibly shapes their answers on Trust, Autonomy and Coverage. A cautious Autonomy score reads differently from someone whose only exposure is inline completion than from someone running agents in Foundry.

Row-5 ticks are a signal about the estate, not about the person.

## What was considered and cut

| Candidate | Outcome |
|---|---|
| Role / discipline | **Cut.** Single-discipline team; would be decoration, and the Coverage grid's N/A pattern is comparable person-to-person without it. |
| Years of professional experience | **Cut entirely**, not even recorded off-survey. The team acts as a team; the experience lens isn't one to apply to these results. |
| AI tenure (how long they've used AI tools) | **Cut.** Tenure is a poor proxy for skill, and Fluency measures the thing directly. |
| Hours per week using AI | **Cut.** Self-reported hours are unreliable, and the underlying question — *when* someone reaches for AI — is the Coverage grid's job at far higher resolution. |
| "Which tools would you like to use more?" | **Cut.** Aspiration belongs to Future-state, which is scored on the Desirability scale across both stances; a product wishlist fits neither. The Coverage grid's future columns carry aspiration about the work. |

Cutting the frequency item leaves a requirement on the Current-state item bank ([#5](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/5)): **Comfort's behaviour items must cover overall frequency of AI use**, so the signal isn't lost.
