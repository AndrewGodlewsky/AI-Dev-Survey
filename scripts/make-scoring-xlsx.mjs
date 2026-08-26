// Builds scoring/scoring.xlsx — the Scoring sheet (#15). Formulas only, no VBA.
//
//   node scripts/make-scoring-xlsx.mjs
//
// Sources of truth it reads:
//   survey/SURVEY.md         — the form's verbatim statement/option text and question order (#13)
//   scoring/scored-sample.csv — the eight fake personas (#12/#20), inverted into fake Forms responses
//                               so the workbook ships with an acceptance test: after Excel recalculates,
//                               the Export sheet must equal scored-sample.csv cell for cell.
//
// Sheets: ReadMe · Config · Responses (shaped like the Forms export) · Items (column ↔ key map) ·
// Values (label → number, one column per statement) · Pattern (#20 flag arithmetic) · Export (the
// 293-column scored CSV, one formula per cell) · Team (mean / range / n, Coverage distributions).
// The workbook is written as raw OOXML (no library): every non-input cell is an <f> formula.

import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { deflateRawSync } from "node:zlib";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const OUT = join(ROOT, "scoring", "scoring.xlsx");

// ------------------------------------------------------------------ keys and scales
const PASSES = ["current", "future-personal", "future-team"];
const DIMS = [
  { key: "comfort",      cur: ["C1", "C2", "C3"],                          fut: ["FC1", "FC2", "FC3"] },
  { key: "trust",        cur: ["T1", "T2", "T3"],                          fut: ["FT1", "FT2", "FT3"] },
  { key: "fluency",      cur: ["F1", "F2", "F3"],                          fut: ["FF1", "FF2", "FF3"] },
  { key: "guardrails",   cur: ["G1", ["G2", "G3"], "G4", "G5", "G6"],      fut: ["FG1", "FG2", "FG3", "FG4", "FG5"] },
  { key: "concern",      cur: ["N1", "N2", "N3", "N4", "N5"],              fut: ["FN1", "FN2", "FN3", "FN4", "FN5"] },
  { key: "autonomy",     cur: ["A1", "A2", "A3"],                          fut: ["FA1", "FA2", "FA3"] },
  { key: "craft-values", cur: ["V1", "V2", "V3"],                          fut: ["FV1", "FV2", "FV3"] },
];
const REV = new Set(["C3", "T2", "F3", "G6", "N4", "A2", "V2", "FC3", "FT2", "FF3", "FG5", "FN4", "FA2", "FV2"]);
const AREAS = ["requirements", "architecture", "production-code", "tests", "code-review", "debugging", "documentation", "refactoring",
  "ci-cd", "infrastructure", "incident-response", "monitoring", "data-migrations", "security-review", "dependency-upgrades",
  "estimates", "stakeholder-comms", "learning", "meeting-notes"];
const SAFEGUARDS = ["read-myself", "another-person", "tests", "rollback", "schema-check", "small-blast-radius", "security-scan"];
const TOOLS = ["copilot", "copilot-studio", "m365-copilot", "azure-ai-foundry", "other-tool"];
const PROBES = ["P1", "P2", "P3", "P4", "P5"];
const SCALES = {
  tool: ["1 – Never used", "2 – Tried it, not using it now", "3 – Use it occasionally", "4 – Use it regularly"],
  behaviour: ["1 – Never", "2 – Rarely", "3 – Sometimes", "4 – Often", "5 – Always"],
  attitude: ["1 – Not at all", "2 – Slightly", "3 – Moderately", "4 – Mostly", "5 – Completely"],
  desirability: ["1 – Definitely not", "2 – Probably not", "3 – Unsure", "4 – Probably", "5 – Definitely"],
  involvement: ["1 – None: no AI", "2 – Advisor: AI explains, I do the work", "3 – Drafter: AI drafts, I rework every line", "4 – Doer, reviewed: AI does it, I review the result", "5 – Doer, spot-checked: AI does it, I spot-check", "6 – System-verified: AI does it, checks catch errors", "N/A – I don't do this work"],
};
const Q_SCALE = { Q1: "tool", Q2: "behaviour", Q3: "involvement", Q4: "attitude", Q5: "attitude", Q7: "desirability", Q8: "desirability", Q9: "involvement", Q11: "desirability", Q12: "desirability", Q13: "involvement" };
const Q_PASS = { Q7: "future-personal", Q8: "future-personal", Q11: "future-team", Q12: "future-team" };
const CHOICE_Q = new Set(["Q6", "Q10", "Q14", "Q15"]);

// ------------------------------------------------------------------ parse SURVEY.md → form columns in order
const survey = readFileSync(join(ROOT, "survey", "SURVEY.md"), "utf8").split(/\r?\n/);
const form = []; // { q, header (Forms column header), key (Values/CSV key), kind, block, rev, label, option }
let q = null, title = null;
for (const line of survey) {
  const mq = line.match(/^### (Q\d+) · (\w+)/); if (mq) { q = mq[1]; title = null; continue; }
  const mt = line.match(/^\*\*Title:\*\* `(.+)`$/); if (mt) { title = mt[1]; continue; }
  const r = line.match(/^\| (\d+) \| ([^|]+) \| (.+?) \|$/); if (!r || !q) continue;
  const id = r[2].trim(), text = r[3].trim();
  if (CHOICE_Q.has(q)) { // one Values column per option: key = the CSV key (safeguard.<s>.<pass> / learn.<s>)
    form.push({ q, header: title, option: text, key: id, kind: id.startsWith("learn") ? "learn" : "safeguard", block: "", rev: 0, label: id });
  } else if (q === "Q1") form.push({ q, header: text, key: "context." + id.replace(/^tool\./, ""), kind: "context", block: "", rev: 0, label: id });
  else if (id.startsWith("area.")) form.push({ q, header: text, key: id, kind: "area", block: "", rev: 0, label: id.replace(/^area\./, "") });
  else if (/^P\d$/.test(id)) form.push({ q, header: text, key: `probe.${id}.${Q_PASS[q]}`, kind: "probe", block: Q_PASS[q], rev: 0, label: id + (Q_PASS[q] === "future-personal" ? "/me" : "/team") });
  else if (q === "Q2") form.push({ q, header: text, key: `item.${id}.current`, kind: "item", block: "", rev: REV.has(id) ? 1 : 0, label: id });
  else if (q === "Q4" || q === "Q5") form.push({ q, header: text, key: `item.${id}.current`, kind: "item", block: "current", rev: REV.has(id) ? 1 : 0, label: id });
  else form.push({ q, header: text, key: `item.${id}.${Q_PASS[q]}`, kind: "item", block: Q_PASS[q], rev: REV.has(id) ? 1 : 0, label: id + (Q_PASS[q] === "future-personal" ? "/me" : "/team") });
}
const formQs = [...new Set(form.map(c => c.q))];
const formHeaders = ["Respondent ID", "Start time", "Completion time", "Respondent name", "Respondent email address",
  ...formQs.flatMap(qq => CHOICE_Q.has(qq) ? [form.find(c => c.q === qq).header] : form.filter(c => c.q === qq).map(c => c.header))];

// Values column order: contiguous blocks so the #20 statistics are plain ranges; survey order inside each
// future block (items and probes interleaved as in the form, identical order in both stance blocks).
const futOrder = b => form.filter(c => c.block === b && (c.kind === "item" || c.kind === "probe"));
const V = [];
for (const c of form.filter(c => c.kind === "context")) V.push(c);
for (const c of form.filter(c => c.kind === "item" && c.block === "current")) V.push(c);
for (const c of form.filter(c => c.kind === "item" && c.block === "")) V.push(c);
for (const c of futOrder("future-personal")) V.push(c);
for (const c of futOrder("future-team")) V.push(c);
for (const c of form.filter(c => c.kind === "area")) V.push(c);
for (const c of form.filter(c => c.kind === "safeguard")) V.push(c);
for (const c of form.filter(c => c.kind === "learn")) V.push(c);
if (V.length !== form.length) throw new Error(`Values columns ${V.length} ≠ form columns ${form.length}`);

// ------------------------------------------------------------------ sample personas → fake Forms responses
const csvText = readFileSync(join(ROOT, "scoring", "scored-sample.csv"), "utf8").replace(/^﻿/, "");
const csv = csvText.split(/\r?\n/).filter(Boolean).map(l => { const out = []; let cur = "", inq = false; for (let i = 0; i < l.length; i++) { const ch = l[i]; if (inq) { if (ch === '"' && l[i + 1] === '"') { cur += '"'; i++; } else if (ch === '"') inq = false; else cur += ch; } else if (ch === '"') inq = true; else if (ch === ",") { out.push(cur); cur = ""; } else cur += ch; } out.push(cur); return out; });
const CSV_HEADER = csv[0], sample = csv.slice(1).map(r => Object.fromEntries(CSV_HEADER.map((h, i) => [h, r[i]])));
const label = (scale, v) => v === "" ? "" : v === "NA" ? SCALES[scale][SCALES[scale].length - 1] : SCALES[scale][Number(v) - 1];
const serial = iso => Math.round((Date.UTC(+iso.slice(0, 4), +iso.slice(5, 7) - 1, +iso.slice(8, 10)) - Date.UTC(1899, 11, 30)) / 86400000);
const responses = sample.map((p, i) => {
  const row = { "Respondent ID": i + 1, "Start time": serial(p.completed) + 0.375, "Completion time": serial(p.completed) + 0.4, "Respondent name": p.respondent, "Respondent email address": p.respondent.toLowerCase().replace(/[^a-z]+/g, ".").replace(/\.$/, "") + "@example.com" };
  for (const qq of formQs) {
    const cols = form.filter(c => c.q === qq);
    if (CHOICE_Q.has(qq)) row[cols[0].header] = cols.filter(c => p[c.key] === "1").map(c => c.option).join("; ");
    else for (const c of cols) row[c.header] = label(Q_SCALE[qq], p[c.key]);
  }
  return row;
});
const N = responses.length;

// ------------------------------------------------------------------ cell helpers
const colL = n => { let s = ""; while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = (n - m - 1) / 26; } return s; };
const xml = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const S = (v, style) => ({ t: "s", v, style });          // inline string
const Nn = (v, style) => ({ t: "n", v, style });         // number
const F = (f, style) => ({ t: "f", v: f, style });       // formula
const AF = (f, style) => ({ t: "af", v: f, style });     // array (CSE) formula

// Values layout: row 1 key · 2 kind · 3 block · 4 reverse · 5 label · 6 Forms header · data from row 7; col A = name, data from col B
const VROW0 = 7, VCOL0 = 2;
const vcol = {}; V.forEach((c, i) => vcol[c.key] = colL(VCOL0 + i));
const vref = (key, r) => `Values!$${vcol[key]}${r}`;
const vLast = colL(VCOL0 + V.length - 1);
const blockRange = (block, r) => { const idx = V.map((c, i) => c.block === block ? i : -1).filter(i => i >= 0); return { first: colL(VCOL0 + idx[0]), last: colL(VCOL0 + idx[idx.length - 1]), n: idx.length, row: r }; };
for (const b of ["current", "future-personal", "future-team"]) { const idx = V.map((c, i) => c.block === b ? i : -1).filter(i => i >= 0); for (let k = 1; k < idx.length; k++) if (idx[k] !== idx[k - 1] + 1) throw new Error(`block ${b} not contiguous`); }

// ------------------------------------------------------------------ sheets
const sheets = {};

// ReadMe
sheets.ReadMe = [
  [S("AI-Dev-Survey — Scoring sheet (wayfinder #15). Formulas only, no macros. Implements rubric/RUBRIC.md and scoring/scoring-rules.md; exports the Scored CSV described in scoring/scored-csv-schema.md.")],
  [],
  [S("How to use")],
  [S("1. Export responses from Microsoft Forms (Responses → Open in Excel). If columns look out of order, use ⋯ → Sync all responses to a new workbook instead.")],
  [S("2. Paste the whole export sheet — header row included — over the Responses sheet here, starting at A1. Columns are matched by header text, so order does not matter; the header text must be exactly the form's statement text (survey/SURVEY.md).")],
  [S("3. Values, Pattern, Export and Team are formulas over one row per response. They ship with eight rows (the fake sample). For more responses, select the last row of Values, Pattern and Export and fill down; for fewer, delete the surplus rows. Rows must be 1:1 with Responses rows 2, 3, 4 …")],
  [S("4. Set Config!roster_n to the team size (the number who could have answered).")],
  [S("5. Export sheet → File → Save As → CSV UTF-8 (Comma delimited) (*.csv). Save it OUTSIDE this repository (scoring/*.csv is git-ignored, but the Forms .xlsx is not — keep that outside too). Drop the CSV on dashboard/index.html.")],
  [],
  [S("Acceptance test")],
  [S("The Responses sheet ships filled with the eight fake personas of scoring/scored-sample.csv, converted back into Forms labels. After a full recalculation, the Export sheet must equal scored-sample.csv cell for cell (RUBRIC §8 shows Sofia Marchetti's arithmetic; Jonas Weber trips the Pattern flags). scripts/make-scoring-xlsx.mjs rebuilds this file.")],
  [],
  [S("Sheets")],
  [S("Config — roster size, schema version, and the three Pattern-flag thresholds (named cells).")],
  [S("Responses — shaped exactly like the Forms export: five built-in columns, then one column per Likert statement or Choice question, values as label text.")],
  [S("Items — every Values column: its CSV key, kind, block, reverse-key flag, short label, the Forms header it is read from, and (for multi-selects) the option text. If the form's wording changes, fix column F here.")],
  [S("Values — one row per response, one column per statement: the label converted to its number (VALUE(LEFT(label,1))), N/A → NA, blank stays blank; multi-selects presence-tested per option. Rows 1–6 are metadata the formulas use.")],
  [S("Pattern — #20: per block, counts per answer, mode of the non-reversed rows, reverse-key agreement, modal share, and the flat / stance-identical flags.")],
  [S("Export — the Scored CSV: 293 columns, header verbatim from the schema, one formula per cell. Numbers stay in General format so nothing is rounded on save.")],
  [S("Team — mean, min, max, range and n per Dimension and pass; Coverage distributions and medians. Read-only summary; the dashboard recomputes these from the CSV.")],
];

// Config
sheets.Config = [
  [S("Setting"), S("Value"), S("Notes")],
  [S("roster_n"), Nn(9), S("Team size — everyone who could have answered. Exported on every row so the dashboard can show 'n of roster'.")],
  [S("schema"), Nn(1), S("Scored CSV schema version. The dashboard refuses any other value.")],
  [S("flat_reverse_slack"), Nn(1), S("#20: a block is flat when its reverse-keyed rows at the mode ≥ (reverse-keyed rows answered − this). 1 → 6 of 7, 4 of 5.")],
  [S("flat_modal_share"), Nn(0.9), S("#20: a block is flat when this share of its rows carry one answer, whatever the mode.")],
  [S("stance_identical_min"), Nn(28), S("#20: stance-identical flag when at least this many of the 30 Future stems match across the Me / Team blocks.")],
];
const NAMES = { roster_n: "Config!$B$2", schema_version: "Config!$B$3", flat_reverse_slack: "Config!$B$4", flat_modal_share: "Config!$B$5", stance_identical_min: "Config!$B$6" };

// Responses
// a blank answer is a truly empty cell, as Forms exports it — not an empty string
sheets.Responses = [formHeaders.map(h => S(h)), ...responses.map(r => formHeaders.map(h => { const v = r[h]; return v === "" ? null : typeof v === "number" ? Nn(v, h.endsWith("time") ? 1 : 0) : S(v); }))];

// Items
sheets.Items = [[S("Key"), S("Kind"), S("Block"), S("Reverse"), S("Label"), S("Forms header"), S("Option text")],
  ...V.map(c => [S(c.key), S(c.kind), S(c.block), Nn(c.rev), S(c.label), S(c.header), S(c.option || "")])];

// Values
{
  const rows = [];
  const meta = [["key", c => S(c.key)], ["kind", c => S(c.kind)], ["block", c => S(c.block)], ["reverse", c => Nn(c.rev)], ["label", c => S(c.label)],
    ["Forms header", (c, i) => F(`INDEX(Items!$F:$F,MATCH(${colL(VCOL0 + i)}$1,Items!$A:$A,0))`)]];
  meta.forEach(([name, fn]) => rows.push([S(name), ...V.map((c, i) => fn(c, i))]));
  for (let r = 0; r < N; r++) {
    const vr = VROW0 + r, rr = r + 2; // Responses row
    const raw = c => `INDEX(Responses!$A$${rr}:$ZZ$${rr},1,MATCH(${vcol[c.key]}$6,Responses!$1:$1,0))`;
    rows.push([F(`Responses!$D$${rr}`), ...V.map(c => (c.kind === "safeguard" || c.kind === "learn")
      ? F(`--ISNUMBER(SEARCH(INDEX(Items!$G:$G,MATCH(${vcol[c.key]}$1,Items!$A:$A,0)),${raw(c)}))`)
      : F(`IF(${raw(c)}&""="","",IF(LEFT(${raw(c)},1)="N","NA",VALUE(LEFT(${raw(c)},1))))`))]);
    void vr;
  }
  sheets.Values = rows;
}

// Pattern — one row per response (row 2 ↔ Values row 7)
const P = {}; // key → Pattern cell (per row: function r → ref)
{
  const head = [S("Respondent")], cols = []; // cols: [key, formulaFn(r)] ; r = Values row
  const push = (key, fn) => { cols.push([key, fn]); head.push(S(key)); };
  const BL = { current: "current", fp: "future-personal", ft: "future-team" };
  for (const [tag, block] of Object.entries(BL)) {
    const b = blockRange(block, 0);
    const rng = r => `Values!$${b.first}${r}:$${b.last}${r}`, revRow = `Values!$${b.first}$4:$${b.last}$4`;
    for (let v = 1; v <= 5; v++) push(`${tag}.c${v}`, r => `SUMPRODUCT((${rng(r)}=${v})*(${revRow}=0))`);
    for (let v = 1; v <= 5; v++) push(`${tag}.a${v}`, r => `SUMPRODUCT((${rng(r)}=${v})*(${revRow}=1))`);
    push(`${tag}.top`, (r, C) => `MAX(${C(`${tag}.c1`)}:${C(`${tag}.c5`)})`);
    push(`${tag}.ntie`, (r, C) => `COUNTIF(${C(`${tag}.c1`)}:${C(`${tag}.c5`)},${C(`${tag}.top`)})`);
    for (let v = 1; v <= 5; v++) push(`${tag}.s${v}`, (r, C) => `IF(${C(`${tag}.c${v}`)}=${C(`${tag}.top`)},IF(AND(${v}=3,${C(`${tag}.ntie`)}>1),999,${C(`${tag}.a${v}`)}*10+${v}),999)`);
    push(`${tag}.mode`, (r, C) => `MATCH(MIN(${C(`${tag}.s1`)}:${C(`${tag}.s5`)}),${C(`${tag}.s1`)}:${C(`${tag}.s5`)},0)`);
    push(`${tag}.agree`, (r, C) => `INDEX(${C(`${tag}.a1`)}:${C(`${tag}.a5`)},${C(`${tag}.mode`)})`);
    push(`${tag}.nrev`, r => `SUMPRODUCT((${revRow}=1)*ISNUMBER(${rng(r)}))`);
    push(`${tag}.share`, r => `MAX(COUNTIF(${rng(r)},1),COUNTIF(${rng(r)},2),COUNTIF(${rng(r)},3),COUNTIF(${rng(r)},4),COUNTIF(${rng(r)},5))/COUNT(${rng(r)})`);
    push(`${tag}.flat`, (r, C) => `--OR(AND(${C(`${tag}.mode`)}<>3,${C(`${tag}.agree`)}>=${C(`${tag}.nrev`)}-flat_reverse_slack),${C(`${tag}.share`)}>=flat_modal_share)`);
  }
  const me = blockRange("future-personal", 0), te = blockRange("future-team", 0);
  push("identical", r => `SUMPRODUCT((Values!$${me.first}${r}:$${me.last}${r}=Values!$${te.first}${r}:$${te.last}${r})*ISNUMBER(Values!$${me.first}${r}:$${me.last}${r})*ISNUMBER(Values!$${te.first}${r}:$${te.last}${r}))`);
  push("copy", (r, C) => `--(${C("identical")}>=stance_identical_min)`);
  const rows = [head];
  const colOf = {}; cols.forEach(([k], i) => colOf[k] = colL(i + 2));
  for (let r = 0; r < N; r++) {
    const vr = VROW0 + r, pr = r + 2, C = k => `${colOf[k]}${pr}`;
    rows.push([F(`Values!$A$${vr}`), ...cols.map(([, fn]) => F(fn(vr, C)))]);
  }
  for (const k of Object.keys(colOf)) P[k] = r => `Pattern!$${colOf[k]}${r}`;
  sheets.Pattern = rows;
}

// Export — header verbatim from the sample CSV; one formula per cell
const ecol = {}; CSV_HEADER.forEach((h, i) => ecol[h] = colL(i + 1));
const E = (key, r) => `$${ecol[key]}${r}`;
function exportCell(key, r) { // r = Export row; Values row = r + 5; Pattern row = r
  const vr = r + VROW0 - 2, pr = r;
  const v = k => vref(k, vr);
  const dimF = (dim, pass) => {
    const d = DIMS.find(x => x.key === dim);
    const facets = pass === "current" ? d.cur : d.fut;
    const refs = facets.flat().map(id => v(`item.${id}.${pass}`));
    const fac = facets.map(f => Array.isArray(f) ? `AVERAGE(${f.map(id => v(`item.${id}.${pass}`)).join(",")})` : (REV.has(f) ? `6-${v(`item.${f}.${pass}`)}` : v(`item.${f}.${pass}`)));
    return `IF(COUNT(${refs.join(",")})<${refs.length},NA(),AVERAGE(${fac.join(",")}))`;
  };
  let m;
  if (key === "schema") return F("schema_version");
  if (key === "respondent") return F(`Values!$A$${vr}`);
  if (key === "completed") return F(`TEXT(Responses!$C$${vr - VROW0 + 2},"yyyy-mm-dd")`);
  if (key === "roster_n") return F("roster_n");
  if (key.startsWith("context.")) return F(v(key));
  if ((m = key.match(/^dimension\.(.+)\.(current|future-personal|future-team)$/))) return F(dimF(m[1], m[2]));
  if ((m = key.match(/^gap\.(.+)\.personal$/))) return F(`IF(OR(ISNA(${E(`dimension.${m[1]}.future-personal`, r)}),ISNA(${E(`dimension.${m[1]}.current`, r)})),NA(),${E(`dimension.${m[1]}.future-personal`, r)}-${E(`dimension.${m[1]}.current`, r)})`);
  if ((m = key.match(/^gap\.(.+)\.stance$/))) return F(`IF(OR(ISNA(${E(`dimension.${m[1]}.future-team`, r)}),ISNA(${E(`dimension.${m[1]}.future-personal`, r)})),NA(),${E(`dimension.${m[1]}.future-team`, r)}-${E(`dimension.${m[1]}.future-personal`, r)})`);
  if (key.startsWith("area.")) return F(v(key));
  if ((m = key.match(/^area-gap\.(.+)\.personal$/))) { const a = E(`area.${m[1]}.future-personal`, r), b = E(`area.${m[1]}.current`, r); return F(`IF(AND(ISNUMBER(${a}),ISNUMBER(${b})),${a}-${b},"NA")`); }
  if ((m = key.match(/^area-gap\.(.+)\.stance$/))) { const a = E(`area.${m[1]}.future-team`, r), b = E(`area.${m[1]}.future-personal`, r); return F(`IF(AND(ISNUMBER(${a}),ISNUMBER(${b})),${a}-${b},"NA")`); }
  if ((m = key.match(/^edge\.(P\d)\.(.+)$/))) { const p = v(`probe.${m[1]}.${m[2]}`); return F(`IF(ISNUMBER(${p}),--(${p}>=4),0)`); }
  if (key.startsWith("safeguard.")) return F(v(key));
  if ((m = key.match(/^lever\.(.+)$/))) return F(`IF(OR(${E("flag.inconsistent-current", r)}=1,${E("flag.inconsistent-future-personal", r)}=1),"NA",--AND(${E(`safeguard.${m[1]}.future-personal`, r)}=1,${E(`safeguard.${m[1]}.current`, r)}=0))`);
  if (key.startsWith("learn.")) return F(v(key));
  if ((m = key.match(/^interest\.(.+)$/))) return F(`--AND(${E(`learn.${m[1]}`, r)}=1,${E(`safeguard.${m[1]}.future-personal`, r)}=0)`);
  if (key === "flag.malformed") { const tj = `_xlfn.TEXTJOIN(";",TRUE,IF((Values!$B$2:$${vLast}$2="item")*(Values!$B${vr}:$${vLast}${vr}=""),Values!$B$5:$${vLast}$5,""))`; return AF(`IF(${tj}="",0,${tj})`); }
  if ((m = key.match(/^flag\.inconsistent-(.+)$/))) { const pass = m[1]; return F(`--AND(${E(`safeguard.read-myself.${pass}`, r)}=1,SUM(${SAFEGUARDS.slice(1).map(s => E(`safeguard.${s}.${pass}`, r)).join(",")})>0)`); }
  if (key === "flag.hold") return F(`--AND(${E("safeguard.read-myself.future-personal", r)}=1,${E("flag.inconsistent-future-personal", r)}=0)`);
  if ((m = key.match(/^flag\.flat-(.+)$/))) return F(P[`${{ current: "current", "future-personal": "fp", "future-team": "ft" }[m[1]]}.flat`](pr));
  if (key === "flag.stance-identical") return F(P.copy(pr));
  if ((m = key.match(/^pattern\.(mode|modal-share|reverse-agree)\.(.+)$/))) { const tag = { current: "current", "future-personal": "fp", "future-team": "ft" }[m[2]]; const stat = { mode: "mode", "modal-share": "share", "reverse-agree": "agree" }[m[1]]; return F(P[`${tag}.${stat}`](pr)); }
  if (key === "pattern.stance-identical") return F(P.identical(pr));
  if (key.startsWith("item.") || key.startsWith("probe.")) return F(v(key));
  throw new Error(`no formula for ${key}`);
}
sheets.Export = [CSV_HEADER.map(h => S(h)), ...Array.from({ length: N }, (_, i) => CSV_HEADER.map(h => exportCell(h, i + 2)))];

// Team
{
  const rng = key => `Export!$${ecol[key]}$2:$${ecol[key]}$500`;
  const rows = [[S("Dimension"), S("Pass"), S("Mean"), S("Min"), S("Max"), S("Range"), S("n"), S("Malformed (excluded)")]];
  for (const d of DIMS) for (const p of PASSES) { const k = `dimension.${d.key}.${p}`;
    rows.push([S(d.key), S(p), F(`IFERROR(_xlfn.AGGREGATE(1,6,${rng(k)}),"")`), F(`IFERROR(_xlfn.AGGREGATE(5,6,${rng(k)}),"")`), F(`IFERROR(_xlfn.AGGREGATE(4,6,${rng(k)}),"")`), F(`IFERROR(_xlfn.AGGREGATE(4,6,${rng(k)})-_xlfn.AGGREGATE(5,6,${rng(k)}),"")`), F(`COUNT(${rng(k)})`), F(`SUMPRODUCT(--ISNA(${rng(k)}))`)]); }
  rows.push([], [S("Dimension"), S("Team personal Gap (mean of gap.*.personal)"), S("Norm gap (mean future-team − mean current)"), S("Stance gap mean")]);
  for (const d of DIMS) rows.push([S(d.key), F(`IFERROR(_xlfn.AGGREGATE(1,6,${rng(`gap.${d.key}.personal`)}),"")`), F(`IFERROR(_xlfn.AGGREGATE(1,6,${rng(`dimension.${d.key}.future-team`)})-_xlfn.AGGREGATE(1,6,${rng(`dimension.${d.key}.current`)}),"")`), F(`IFERROR(_xlfn.AGGREGATE(1,6,${rng(`gap.${d.key}.stance`)}),"")`)]);
  rows.push([], [S("Area"), S("Pass"), S("1 None"), S("2 Advisor"), S("3 Drafter"), S("4 Doer, reviewed"), S("5 Doer, spot-checked"), S("6 System-verified"), S("N/A"), S("n"), S("Median (lower middle)")]);
  for (const a of AREAS) for (const p of PASSES) { const k = `area.${a}.${p}`;
    rows.push([S(a), S(p), ...[1, 2, 3, 4, 5, 6].map(l => F(`COUNTIF(${rng(k)},${l})`)), F(`COUNTIF(${rng(k)},"NA")`), F(`COUNT(${rng(k)})`), F(`IF(COUNT(${rng(k)})=0,"",SMALL(${rng(k)},INT((COUNT(${rng(k)})+1)/2)))`)]); }
  rows.push([], [S("Area"), S("Coverage Gap — median of within-person moves (levels)"), S("pairs"), S("Stance gap — median (levels)"), S("pairs")]);
  for (const a of AREAS) { const g = rng(`area-gap.${a}.personal`), s = rng(`area-gap.${a}.stance`);
    rows.push([S(a), F(`IF(COUNT(${g})=0,"",SMALL(${g},INT((COUNT(${g})+1)/2)))`), F(`COUNT(${g})`), F(`IF(COUNT(${s})=0,"",SMALL(${s},INT((COUNT(${s})+1)/2)))`), F(`COUNT(${s})`)]); }
  sheets.Team = rows;
}

// ------------------------------------------------------------------ OOXML
const SHEET_ORDER = ["ReadMe", "Config", "Responses", "Items", "Values", "Pattern", "Export", "Team"];
function sheetXml(rows) {
  let out = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheetData>';
  rows.forEach((row, ri) => {
    if (!row || !row.length) return;
    out += `<row r="${ri + 1}">`;
    row.forEach((cell, ci) => {
      if (cell == null) return;
      const ref = `${colL(ci + 1)}${ri + 1}`, st = cell.style ? ` s="${cell.style}"` : "";
      if (cell.t === "s") out += `<c r="${ref}" t="inlineStr"${st}><is><t xml:space="preserve">${xml(cell.v)}</t></is></c>`;
      else if (cell.t === "n") out += `<c r="${ref}"${st}><v>${cell.v}</v></c>`;
      else if (cell.t === "f") out += `<c r="${ref}"${st}><f>${xml(cell.v)}</f></c>`;
      else if (cell.t === "af") out += `<c r="${ref}"${st}><f t="array" ref="${ref}">${xml(cell.v)}</f></c>`;
    });
    out += "</row>";
  });
  return out + "</sheetData></worksheet>";
}
const files = {};
files["[Content_Types].xml"] = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>${SHEET_ORDER.map((_, i) => `<Override PartName="/xl/worksheets/sheet${i + 1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>`).join("")}</Types>`;
files["_rels/.rels"] = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>`;
files["xl/workbook.xml"] = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>${SHEET_ORDER.map((n, i) => `<sheet name="${n}" sheetId="${i + 1}" r:id="rId${i + 1}"/>`).join("")}</sheets><definedNames>${Object.entries(NAMES).map(([n, ref]) => `<definedName name="${n}">${ref}</definedName>`).join("")}</definedNames><calcPr fullCalcOnLoad="1"/></workbook>`;
files["xl/_rels/workbook.xml.rels"] = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">${SHEET_ORDER.map((_, i) => `<Relationship Id="rId${i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet${i + 1}.xml"/>`).join("")}<Relationship Id="rId${SHEET_ORDER.length + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>`;
files["xl/styles.xml"] = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts><fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills><borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="22" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/></cellXfs></styleSheet>`;
SHEET_ORDER.forEach((n, i) => files[`xl/worksheets/sheet${i + 1}.xml`] = sheetXml(sheets[n]));

// ------------------------------------------------------------------ zip (deflate)
function crc32(buf) { let c, crc = 0xFFFFFFFF; for (let i = 0; i < buf.length; i++) { c = (crc ^ buf[i]) & 0xFF; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; crc = (crc >>> 8) ^ c; } return (crc ^ 0xFFFFFFFF) >>> 0; }
function zip(entries) {
  const parts = [], central = []; let offset = 0;
  for (const [name, text] of entries) {
    const data = Buffer.from(text, "utf8"), comp = deflateRawSync(data), nm = Buffer.from(name, "utf8"), crc = crc32(data);
    const lh = Buffer.alloc(30); lh.writeUInt32LE(0x04034b50, 0); lh.writeUInt16LE(20, 4); lh.writeUInt16LE(0, 6); lh.writeUInt16LE(8, 8); lh.writeUInt16LE(0, 10); lh.writeUInt16LE(0x21, 12); lh.writeUInt32LE(crc, 14); lh.writeUInt32LE(comp.length, 18); lh.writeUInt32LE(data.length, 22); lh.writeUInt16LE(nm.length, 26); lh.writeUInt16LE(0, 28);
    parts.push(lh, nm, comp);
    const ch = Buffer.alloc(46); ch.writeUInt32LE(0x02014b50, 0); ch.writeUInt16LE(20, 4); ch.writeUInt16LE(20, 6); ch.writeUInt16LE(0, 8); ch.writeUInt16LE(8, 10); ch.writeUInt16LE(0, 12); ch.writeUInt16LE(0x21, 14); ch.writeUInt32LE(crc, 16); ch.writeUInt32LE(comp.length, 20); ch.writeUInt32LE(data.length, 24); ch.writeUInt16LE(nm.length, 28); ch.writeUInt16LE(0, 30); ch.writeUInt16LE(0, 32); ch.writeUInt16LE(0, 34); ch.writeUInt16LE(0, 36); ch.writeUInt32LE(0, 38); ch.writeUInt32LE(offset, 42);
    central.push(ch, nm); offset += lh.length + nm.length + comp.length;
  }
  const cd = Buffer.concat(central), end = Buffer.alloc(22); end.writeUInt32LE(0x06054b50, 0); end.writeUInt16LE(0, 4); end.writeUInt16LE(0, 6); end.writeUInt16LE(entries.length, 8); end.writeUInt16LE(entries.length, 10); end.writeUInt32LE(cd.length, 12); end.writeUInt32LE(offset, 16); end.writeUInt16LE(0, 20);
  return Buffer.concat([...parts, cd, end]);
}
writeFileSync(OUT, zip(Object.entries(files)));
const nCells = Object.values(sheets).reduce((s, rows) => s + rows.reduce((t, r) => t + (r ? r.filter(c => c && (c.t === "f" || c.t === "af")).length : 0), 0), 0);
console.log(`${OUT}: ${SHEET_ORDER.length} sheets · Responses ${formHeaders.length} cols × ${N} rows · Values ${V.length} cols · Export ${CSV_HEADER.length} cols · ${nCells} formulas`);
