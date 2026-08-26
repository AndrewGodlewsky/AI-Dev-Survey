# Microsoft Forms — response export shape

Research for wayfinder ticket [#10](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/10).
Gathered 2026-08-26.

**Source grading** used throughout: **[P]** primary (Microsoft product documentation),
**[Q]** Microsoft Q&A / Tech Community — first-party *platform*, community or support-engineer
*answer*, **[U]** unverified, needs an empirical check.

---

## Summary — what changes because of this

Three findings alter decisions already made. Everything else confirms an assumption.

1. **A Likert question's parent text is NOT exported — only the statement (row) text.** The
   Future-state section as designed in [#6](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/6)
   (one Likert per item, two rows *For me* / *For the team*) would export **60 columns headed
   only "For me" or "For the team"**, with nothing saying which item each belongs to. The
   section has to be restructured — see §3.
2. **Likert answers export as the option's label text, not a number.** The Scoring sheet's
   first step is a text→value lookup, before any `6 − answer` from
   [#9](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/9) can run.
3. **Response columns are known to come back out of order** relative to the questions. The
   Scoring sheet must resolve columns **by header text, never by position**.

And the confirmation: **[#19](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/19)'s
load-bearing assumption was right.** Forms' Likert is single-select per row, so the Safeguard
multi-select cannot be a stance grid and stays three separate Choice questions.

---

## 1. Built-in columns

The exported workbook has **one row per response**. The first five columns are fixed: **[P]**

| # | Column |
|---|---|
| 1 | Respondent ID |
| 2 | Start time |
| 3 | Completion time |
| 4 | Respondent name |
| 5 | Respondent email address |

> "Details of each question in your form are represented in columns and each response is shown
> in a row." … "Names and email addresses won't be displayed if you allow your form to accept
> anonymous responses."
> — [Check and share your form results](https://support.microsoft.com/en-us/office/check-and-share-your-form-results-02859424-341d-406f-b32a-9a0fbaf357af) **[P]**

**Consequence:** the form must be configured to **record the name** — the survey is named by
decision, and anonymous mode empties columns 4 and 5. Respondent name is the join key for
every named view in the dashboard.

## 2. Likert is single-select per row — #19 confirmed

> "A Likert type question displays a list of **single-answer questions** and a rating scale for
> the answers, so a respondent can select a value from the scale to answer each question."
> — [Available question types](https://learn.microsoft.com/dynamics365/customer-voice/available-question-types) **[P]** *(Dynamics 365 Customer Voice; same question type and wording as Forms)*

> "Likert in Microsoft Forms can only have 1 option per statement."
> — [Microsoft Q&A](https://learn.microsoft.com/en-ca/answers/questions/2337760/microsoft-forms-query-on-likert-question) **[Q]**

A long-running request thread asks for multi-select Likert rows and has **no official response
and no product change** as of this date —
[Why don't Forms (Office 365) support Likert with multiple answers?](https://learn.microsoft.com/en-us/answers/questions/62c77237-f5f5-4f36-8927-42c411dd703c/why-dont-forms-office-365-support-likert-with) **[Q]**

**So:** the Safeguard items stay **three separate Choice questions with Multiple answers
enabled**, exactly as `survey/safeguard-items.md` assumed. The hoped-for shortening doesn't
exist. The Coverage grid is fine as a native Likert — 19 statements × 6 levels + N/A, one
selection per row is what it needs.

## 3. Likert exports one column per statement — and drops the question text

This is the finding that forces a redesign.

> "the **question is NOT exported** along with the items. E.G., the 'Session 1' vs 'session 2'
> text is NOT exported and ONLY the likert statement … The only way I can tell which statements
> go with which question is by knowing the exact order."
> — [Export Likert Question Text with Statements](https://techcommunity.microsoft.com/discussions/microsoftforms/export-likert-question-text-with-statements/3809962) **[Q]**

Each statement becomes its own column, headed with **the statement text alone**.

**What this breaks.** #6 designed each Future-state item as one Likert block with two rows:

```
In six months…                          | Definitely not | … | Definitely |
  For me                                |                |   |            |
  For the team                          |                |   |            |
```

Exported, that is two columns headed `For me` and `For the team` — repeated **thirty times**,
with the item stem nowhere in the workbook.

**The fix — one Likert block per stance, statements are the item stems:**

| Block | Statements | Column headers |
|---|---|---|
| "In six months, **I would**…" | all 30 stems | the stem text — unique |
| "In six months, **the team should**…" | the same 30 stems | the stem text — **collides with block 1** |

The stems are identical across the two blocks, so the headers still collide. **Every statement
text in the whole form must be unique**, which means the stance has to be carried inside the
statement — e.g. `[Me] …use AI in most development work.` and
`[Team] …use AI in most development work.` — or each stem given a short unique code.

**This is a real cost of the two-stance design and it lands on
[#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13).** It also means item wording
is no longer purely a readability question: **item text is the database key.**

Uniqueness matters within the Current section too — no two statements anywhere may match.

## 4. Answers export as label text, not numbers

> "the Likert response columns contain the text labels of the options (like 'Strongly Agree',
> 'Agree') rather than numeric values, requiring post-processing in Excel if you need numeric
> encoding." — corroborated across [Q] threads; the standard advice is `VLOOKUP`/`IF` mapping
> after export. **[Q]**

Microsoft Forms does not attach weights to Likert options.

**Consequence for [#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15):** the
Scoring sheet's **first** step is a label→value lookup table, before reverse-keying, facet
means, or anything else in `scoring/scoring-rules.md`. Three lookup tables are needed — the
behaviour scale, the attitude scale, the Desirability scale — plus the Involvement levels and
the Context item's four states.

**A cheaper option worth considering at [#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13):**
prefix the option labels with their number — `1 – Never`, `2 – Rarely` … — so the value can be
read off the front of the string instead of matched against a table. A Microsoft support
engineer recommended exactly this for a related problem **[Q]**. The cost is a slightly
noisier-looking scale for Respondents; the benefit is that the sheet stops depending on exact
label text, which is otherwise a silent break the first time anyone edits a word.

*(A related thread — [missing values in Likert export](https://learn.microsoft.com/en-us/answers/questions/5361934/(forms)-missing-values-in-likert-scale-excel-expor) **[Q]** — turns out to be about scales with unlabelled middle options, confirmed as expected behaviour, not a bug. Every scale in this survey labels all five points, so it doesn't apply.)*

## 5. Column order is not guaranteed

> **Symptom:** "the response columns are out of order in the response workbook … compared to
> the order of the questions on the form." **Cause:** "This is a known issue that's being
> investigated." **Workaround:** Responses → ellipses → *Sync all responses to a new workbook*.
> — [Forms response columns are out of order](https://learn.microsoft.com/troubleshoot/microsoft-365-apps/microsoft-forms/forms-response-columns-out-of-order) **[P]**

**Consequence for #15:** the Scoring sheet must locate every column **by header text**
(`MATCH` / `XLOOKUP` on the header row), never by fixed position. Combined with §3, this makes
statement text load-bearing twice over.

## 6. Multi-select answers land in one delimited cell

All selected options come back in a **single cell**. The delimiter is where the sources
disagree:

- A Microsoft Q&A thread shows **comma-space**: *"the results appear in a single cell as a
  comma-separated list (e.g., 'Beaker, Microscope, Scale')"* — and the accepted answer treats
  splitting on a comma as the normal approach.
  [Q&A](https://learn.microsoft.com/answers/a/12851015) **[Q]**
- Secondary write-ups claim **semicolon**. **[U]**

**Unresolved — and it does not need resolving.** The Safeguard options contain commas and
parentheses of their own (*"The blast radius is small (docs, internal tooling,
non-production)"*), so splitting on **any** delimiter is fragile regardless of which one Forms
uses.

**Recommendation for #15: don't split. Test for presence.** One column per option, each
`=ISNUMBER(SEARCH("<option text>", <cell>))`. This is delimiter-agnostic, survives a change of
delimiter, and turns the multi-select straight into the binary columns the scored CSV
([#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12)) wants anyway.

**One constraint it imposes:** no option text may be a substring of another, or the shorter one
will match inside the longer. The seven Safeguard options are currently distinct on that test —
worth re-checking if any are reworded.

**Still worth confirming empirically** (§8) since it costs five minutes.

## 7. Size — the survey fits, with room

> "For the Likert question type, **each 'statement' counts as a single question**." Limit:
> **up to 200 questions per form**.
> — [Form, question, response, and character limits](https://support.microsoft.com/en-us/forms/form-question-response-and-character-limits-in-microsoft-forms) **[P]**

| Block | Statements / questions |
|---|---|
| Context tools matrix | 5 |
| Current-state Dimension items | 26 |
| Coverage grid — Today | 19 |
| Future-state items + probes, **× 2 stance blocks** | 60 |
| Coverage grid — 6 months for me / the team | 38 |
| Safeguard items 1–4 | 4 |
| **Total** | **152 of 200** |

48 questions of headroom. Not a constraint today, but it is a ceiling — worth knowing before
[#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20) considers adding attention
checks.

Character limits are not a risk: 4,000 per question, 1,000 per choice option.

## 8. Sample header row

What the Scoring sheet should expect. Statement text shown as it would need to be written for
§3's uniqueness rule.

```
Respondent ID | Start time | Completion time | Respondent name | Respondent email address |
GitHub Copilot | Copilot Studio | Microsoft 365 Copilot | Azure AI Foundry | Another AI tool not on this list |
How often do you use an AI tool in your development work? |
How often do you use AI on work that ends up in production? |
… (24 more Current-state statements) …
[Today] Requirements & ideation | [Today] Architecture & design | … (17 more) |
Which of these, if any, do you accept today instead of reading AI's output yourself? |
[Me] …use AI in most development work. | [Me] …use AI on work that ends up in production. | … (28 more) |
[Team] …use AI in most development work. | … (29 more) |
[6mo-me] Requirements & ideation | … | [6mo-team] Requirements & ideation | … |
In six months, which of these would you accept instead of reading AI's output yourself? | …
```

Cell values are **label text**: `Often`, `Mostly`, `Probably`, `Doer, reviewed — AI does it, I
review the result`, `N/A — I don't do this work`, and for multi-selects a single delimited
string of the selected option labels.

Note the Involvement level labels contain a comma and an em-dash — another reason §6's
presence-test approach beats splitting, and a reason the lookup table in §4 must match the
label **exactly** as Forms writes it.

## 9. Verified by reading; not yet verified by doing

Everything above comes from documentation and first-party threads. Four things are cheap to
confirm with a **throwaway 6-question form and two submitted responses**, and are worth
confirming before #15 is built:

1. The **multi-select delimiter** — comma-space or semicolon (§6). Moot if the presence-test
   approach is taken, decisive if it isn't.
2. Whether two Likert **statements with identical text** in different blocks produce two
   distinguishable columns or one merged/suffixed one (§3). Determines whether the `[Me]` /
   `[Team]` prefixes are required or merely tidy.
3. The **exact label strings** for Involvement levels as exported — whether the em-dash and the
   help text survive into the header/value.
4. Whether **Required** on a Likert applies per statement or per question — i.e. whether a
   Respondent can submit with one row of a grid unanswered. This is directly load-bearing:
   #9 decided a blank is a malformed export rather than data, and that rests on Required making
   blanks unreachable.

Item 4 is the one that could change a decision. The others change implementation only.

## 10. What this hands downstream

- **[#12](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/12) Scored CSV** — join key is **Respondent name**; multi-selects become binary columns per option (§6).
- **[#13](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/13) Survey document** — **every statement text in the form must be unique** (§3), which forces stance prefixes on the 60 Future-state statements; the form must record names (§1); consider numbering the scale option labels (§4); Safeguard items are three separate Choice questions, not a grid (§2).
- **[#15](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/15) Scoring sheet** — label→value lookup runs first (§4); resolve columns by header text, never position (§5); presence-test multi-selects rather than splitting (§6); re-sync the workbook if columns look wrong (§5).
- **[#20](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/20) Straight-lining** — 48 questions of headroom against the 200 limit (§7).
- **[#18](https://github.com/AndrewGodlewsky/AI-Dev-Survey/issues/18) Pilot** — the four checks in §9 fold naturally into the pilot, but #15 needs at least check 4 answered before it starts.
