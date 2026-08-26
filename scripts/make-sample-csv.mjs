// Generates scoring/scored-sample.csv — the fixture for the dashboard (#16) and the worked
// example for scoring/scored-csv-schema.md (#12). Eight FAKE personas; names are invented.
//
//   node scripts/make-sample-csv.mjs
//
// This is a fixture generator, not the reference scorer: the Excel Scoring sheet (#15) is the
// reference implementation of scoring/scoring-rules.md. The personas and the scoring below are
// lifted from the throwaway prototype for #11 so the sample exercises every column family:
// a NA, a mixed N/A pair, an inconsistent safeguard answer, Edge markers in all three states,
// Levers, a principle hold, a malformed (blank) item, and (#20) a flat-lined + block-copied
// Future section that trips the Pattern flags.

import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const OUT = join(dirname(fileURLToPath(import.meta.url)), "..", "scoring", "scored-sample.csv");
const SCHEMA = 1, ROSTER_N = 9;
const PASSES = ["current", "future-personal", "future-team"];

// ---- keys (the key table in the spec) -------------------------------------------------------
const DIMS = [
  { key: "comfort",      cur: ["C1", "C2", "C3"],              fut: ["FC1", "FC2", "FC3"] },
  { key: "trust",        cur: ["T1", "T2", "T3"],              fut: ["FT1", "FT2", "FT3"] },
  { key: "fluency",      cur: ["F1", "F2", "F3"],              fut: ["FF1", "FF2", "FF3"] },
  { key: "guardrails",   cur: ["G1", ["G2", "G3"], "G4", "G5", "G6"], fut: ["FG1", "FG2", "FG3", "FG4", "FG5"] },
  { key: "concern",      cur: ["N1", "N2", "N3", "N4", "N5"],  fut: ["FN1", "FN2", "FN3", "FN4", "FN5"] },
  { key: "autonomy",     cur: ["A1", "A2", "A3"],              fut: ["FA1", "FA2", "FA3"] },
  { key: "craft-values", cur: ["V1", "V2", "V3"],              fut: ["FV1", "FV2", "FV3"] },
];
const REV = new Set(["C3", "T2", "F3", "G6", "N4", "A2", "V2", "FC3", "FT2", "FF3", "FG5", "FN4", "FA2", "FV2"]);
const AREAS = ["requirements", "architecture", "production-code", "tests", "code-review", "debugging", "documentation", "refactoring",
  "ci-cd", "infrastructure", "incident-response", "monitoring", "data-migrations", "security-review", "dependency-upgrades",
  "estimates", "stakeholder-comms", "learning", "meeting-notes"];
const GROUP_OF = i => (i < 8 ? 0 : i < 12 ? 1 : i < 15 ? 2 : 3);
const SAFEGUARDS = ["read-myself", "another-person", "tests", "rollback", "schema-check", "small-blast-radius", "security-scan"];
const TOOLS = ["copilot", "copilot-studio", "m365-copilot", "azure-ai-foundry", "other-tool"];
const PROBES = ["P1", "P2", "P3", "P4", "P5"];

// ---- fake personas (from the #11 prototype) --------------------------------------------------
// dims: [current, future-personal, future-team] targets · probes: [personal, team] · cov: base level per
// area group, dMe/dTeam future shift, over: area index → [cur, fp, ft] (null = N/A), na: N/A everywhere ·
// safe: indices into SAFEGUARDS · tools: 1–4 per TOOLS row · blank: item left blank (malformed export)
const PERSONAS = [
  { name: "Maya Okafor",     completed: "2026-09-14", tools: [4, 2, 3, 4, 4], dims: { comfort: [4.6, 4.9, 4.4], trust: [4.1, 4.6, 3.7], fluency: [4.5, 4.8, 4.4], guardrails: [1.8, 1.7, 2.4], concern: [1.7, 1.9, 2.3], autonomy: [4.2, 4.8, 3.9], "craft-values": [2.9, 2.7, 3.3] },
    probes: { P1: [1, 1], P2: [5, 4], P3: [5, 5], P4: [1, 1], P5: [2, 2] }, cov: { base: [4, 3, 3, 5], dMe: 1, dTeam: 1, over: { 4: [5, 6, 6], 13: [4, 5, 4] }, na: [] }, safe: { cur: [2, 3, 6], fp: [2, 3, 4, 6], ft: [2, 3, 6], learn: [4, 5] } },
  { name: "Tom Lindqvist",   completed: "2026-09-14", tools: [2, 2, 1, 1, 1], dims: { comfort: [2.0, 2.2, 2.6], trust: [1.5, 1.8, 2.0], fluency: [2.6, 3.2, 3.4], guardrails: [4.5, 4.7, 4.6], concern: [4.4, 4.5, 4.3], autonomy: [1.6, 1.8, 2.2], "craft-values": [4.8, 4.9, 4.8] },
    probes: { P1: [4, 2], P2: [1, 1], P3: [1, 1], P4: [4, 4], P5: [5, 5] }, cov: { base: [2, 1, 2, 2], dMe: 0, dTeam: 0, over: { 17: [3, 3, 3] }, na: [9, 10] }, safe: { cur: [0], fp: [0], ft: [0], learn: [4] } },
  { name: "Priya Raman",     completed: "2026-09-15", tools: [4, 1, 3, 4, 2], dims: { comfort: [4.0, 4.7, 3.8], trust: [3.4, 4.4, 3.2], fluency: [4.0, 4.6, 4.0], guardrails: [2.6, 2.2, 3.2], concern: [2.4, 2.3, 3.0], autonomy: [3.4, 4.7, 3.0], "craft-values": [3.6, 3.4, 3.8] },
    probes: { P1: [1, 1], P2: [4, 2], P3: [5, 2], P4: [1, 2], P5: [3, 3] }, cov: { base: [4, 2, 3, 4], dMe: 1, dTeam: 0, over: { 2: [4, 5, 4], 3: [4, 6, 4] }, na: [11] }, safe: { cur: [2, 5], fp: [2, 3, 5, 6], ft: [2, 5], learn: [4] } },
  { name: "Daniel Cho",      completed: "2026-09-15", tools: [4, 2, 3, 1, 1], dims: { comfort: [3.2, 3.5, 4.2], trust: [2.8, 3.0, 3.8], fluency: [3.1, 3.6, 4.0], guardrails: [3.4, 3.4, 3.0], concern: [3.0, 3.0, 2.6], autonomy: [2.4, 2.7, 3.6], "craft-values": [3.9, 3.9, 3.6] },
    probes: { P1: [2, 2], P2: [2, 4], P3: [2, 4], P4: [2, 2], P5: [4, 3] }, cov: { base: [3, 2, 2, 3], dMe: 0, dTeam: 1, over: {}, na: [10, 13] }, safe: { cur: [1], fp: [1, 2], ft: [1, 2, 6], learn: [3, 4] } },
  { name: "Sofia Marchetti", completed: "2026-09-16", tools: [3, 1, 4, 2, 1], dims: { comfort: [3.0, 4.4, 4.2], trust: [2.6, 3.9, 3.8], fluency: [2.8, 4.2, 4.1], guardrails: [3.2, 3.0, 3.1], concern: [3.2, 2.8, 2.9], autonomy: [2.4, 3.9, 3.8], "craft-values": [3.5, 3.5, 3.5] },
    probes: { P1: [2, 1], P2: [3, 3], P3: [3, 3], P4: [2, 2], P5: [3, 3] }, cov: { base: [3, 3, 2, 3], dMe: 1, dTeam: 1, over: { 13: [null, 3, 3] }, na: [9] }, safe: { cur: [1], fp: [0, 2], ft: [2, 3], learn: [4, 5] } },
  { name: "Liam O'Connor",   completed: "2026-09-16", tools: [4, 1, 2, 2, 4], dims: { comfort: [3.8, 3.6, 3.7], trust: [3.2, 2.6, 2.9], fluency: [4.2, 4.3, 4.1], guardrails: [3.0, 3.6, 3.7], concern: [3.4, 3.8, 3.6], autonomy: [3.8, 3.0, 3.2], "craft-values": [4.1, 4.3, 4.2] },
    probes: { P1: [3, 2], P2: [2, 2], P3: [2, 2], P4: [3, 4], P5: [4, 4] }, cov: { base: [3, 4, 3, 3], dMe: 0, dTeam: 0, over: { 10: [5, 4, 4], 11: [6, 6, 5], 18: [3, null, null] }, na: [0] }, safe: { cur: [2, 3, 6], fp: [2, 3], ft: [2, 3, 6], learn: [] } },
  { name: "Aisha Bello",     completed: "2026-09-17", tools: [3, 1, 4, 1, 1], dims: { comfort: [3.1, 4.0, 4.0], trust: [2.9, 3.4, 3.5], fluency: [2.0, 4.4, 4.2], guardrails: [3.3, 3.3, 3.4], concern: [2.7, 2.7, 2.9], autonomy: [2.0, 3.2, 3.3], "craft-values": [3.4, 3.6, 3.6] },
    probes: { P1: [2, 2], P2: [2, 2], P3: [2, 3], P4: [2, 2], P5: [3, 3] }, cov: { base: [2, 1, 1, 3], dMe: 1, dTeam: 1, over: { 16: [3, 4, 4] }, na: [9, 10, 12, 13] }, safe: { cur: [0], fp: [1, 2], ft: [1, 2], learn: [2, 4, 6] },
    blank: "N3" }, // one malformed item, so the sample shows #N/A + flag.malformed
  // #20: a tired respondent — considered Current answers, then a flat "Probably" down the [Me] block and the
  // [Team] block copied from it. Trips flag.flat-future-personal, flag.flat-future-team and flag.stance-identical;
  // his Current block stays clean. Appended LAST so the seven rows above are unchanged (the RNG is sequential).
  { name: "Jonas Weber",     completed: "2026-09-18", tools: [3, 1, 2, 1, 1], dims: { comfort: [3.4, 4, 4], trust: [3.0, 4, 4], fluency: [3.3, 4, 4], guardrails: [3.1, 4, 4], concern: [2.9, 4, 4], autonomy: [2.8, 4, 4], "craft-values": [3.6, 4, 4] },
    probes: { P1: [4, 4], P2: [4, 4], P3: [4, 4], P4: [4, 4], P5: [4, 4] }, cov: { base: [3, 2, 2, 3], dMe: 1, dTeam: 1, over: {}, na: [10] }, safe: { cur: [2], fp: [2, 3], ft: [2, 3], learn: [4] },
    flat: { "future-personal": 4, copyTeam: true } },
];

// ---- #20 Pattern flags: the blocks the rule reads (scoring/scoring-rules.md §6.1) -------------------
// current = the 17 Attitude-scale items (the 9 Behaviour items are on another scale and carry only two
// reverse-keys); future-* = the 25 items + 5 probes of one stance block. Probes count as rows but are never
// reverse-keyed, so they sit in the modal share and outside the reverse-key agreement.
const ATTITUDE = ["C3", "T1", "T3", "F3", "G1", "G2", "G4", "G5", "G6", "N1", "N2", "N3", "N4", "N5", "V1", "V2", "V3"];
const FUT_ITEMS = DIMS.flatMap(d => d.fut);
const THRESH = { reverseSlack: 1, modalShare: 0.90, stanceIdentical: 28 }; // the sheet's three input cells

// ---- deterministic item generation ------------------------------------------------------------
function rng(seed) { return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const r = rng(20260826); const noise = () => (r() - 0.5) * 1.3;

function generate(P) {
  const item = {}; // item[id][pass]
  for (const d of DIMS) {
    const [tc, tp, tt] = P.dims[d.key];
    for (const f of d.cur.flat()) { const v = clamp(Math.round(tc + noise()), 1, 5); item[f] = { current: REV.has(f) ? 6 - v : v }; }
    for (const f of d.fut) { const v1 = clamp(Math.round(tp + noise()), 1, 5), v2 = clamp(Math.round(tt + noise()), 1, 5); item[f] = { "future-personal": REV.has(f) ? 6 - v1 : v1, "future-team": REV.has(f) ? 6 - v2 : v2 }; }
  }
  if (P.blank) item[P.blank].current = null;
  if (P.flat) { for (const f of FUT_ITEMS) { if (P.flat["future-personal"]) item[f]["future-personal"] = P.flat["future-personal"]; if (P.flat.copyTeam) item[f]["future-team"] = item[f]["future-personal"]; } }
  const area = AREAS.map((_, i) => {
    if (P.cov.na.includes(i)) return { current: null, "future-personal": null, "future-team": null };
    if (P.cov.over[i]) { const [c, p, t] = P.cov.over[i]; return { current: c, "future-personal": p, "future-team": t }; }
    const c = clamp(P.cov.base[GROUP_OF(i)] + (r() < 0.25 ? (r() < 0.5 ? -1 : 1) : 0), 1, 6);
    return { current: c, "future-personal": clamp(c + P.cov.dMe + (r() < 0.2 ? 1 : 0), 1, 6), "future-team": clamp(c + P.cov.dTeam + (r() < 0.2 ? 1 : 0), 1, 6) };
  });
  return { item, area };
}

// ---- scoring (scoring/scoring-rules.md) --------------------------------------------------------
const mean = xs => xs.reduce((a, b) => a + b, 0) / xs.length;
const val = (item, f, pass) => { const a = item[f][pass]; return a == null ? null : REV.has(f) ? 6 - a : a; };
function score(item, facets, pass) {
  const fv = facets.map(f => { const vs = (Array.isArray(f) ? f : [f]).map(x => val(item, x, pass)); return vs.includes(null) ? null : mean(vs); });
  return fv.includes(null) ? "#N/A" : mean(fv);
}
const sub = (a, b) => (typeof a === "number" && typeof b === "number") ? a - b : (a === "#N/A" || b === "#N/A") ? "#N/A" : "NA";

// ---- build rows -------------------------------------------------------------------------------
const header = ["schema", "respondent", "completed", "roster_n",
  ...TOOLS.map(t => `context.${t}`),
  ...DIMS.flatMap(d => PASSES.map(p => `dimension.${d.key}.${p}`)),
  ...DIMS.flatMap(d => [`gap.${d.key}.personal`, `gap.${d.key}.stance`]),
  ...AREAS.flatMap(a => PASSES.map(p => `area.${a}.${p}`)),
  ...AREAS.flatMap(a => [`area-gap.${a}.personal`, `area-gap.${a}.stance`]),
  ...PROBES.flatMap(p => [`edge.${p}.future-personal`, `edge.${p}.future-team`]),
  ...SAFEGUARDS.flatMap(s => PASSES.map(p => `safeguard.${s}.${p}`)),
  ...SAFEGUARDS.slice(1).map(s => `lever.${s}`),
  ...SAFEGUARDS.slice(1).map(s => `learn.${s}`),
  ...SAFEGUARDS.slice(1).map(s => `interest.${s}`),
  "flag.malformed", "flag.inconsistent-current", "flag.inconsistent-future-personal", "flag.inconsistent-future-team", "flag.hold",
  "flag.flat-current", "flag.flat-future-personal", "flag.flat-future-team", "flag.stance-identical",
  ...PASSES.map(p => `pattern.mode.${p}`), ...PASSES.map(p => `pattern.modal-share.${p}`), ...PASSES.map(p => `pattern.reverse-agree.${p}`), "pattern.stance-identical",
  ...DIMS.flatMap(d => d.cur.flat().map(f => `item.${f}.current`)),
  ...DIMS.flatMap(d => d.fut.flatMap(f => [`item.${f}.future-personal`, `item.${f}.future-team`])),
  ...PROBES.flatMap(p => [`probe.${p}.future-personal`, `probe.${p}.future-team`]),
];

const rows = PERSONAS.map(P => {
  const { item, area } = generate(P);
  const row = { schema: SCHEMA, respondent: P.name, completed: P.completed, roster_n: ROSTER_N };
  TOOLS.forEach((t, i) => row[`context.${t}`] = P.tools[i]);
  for (const d of DIMS) {
    const s = { current: score(item, d.cur, "current"), "future-personal": score(item, d.fut, "future-personal"), "future-team": score(item, d.fut, "future-team") };
    PASSES.forEach(p => row[`dimension.${d.key}.${p}`] = s[p]);
    row[`gap.${d.key}.personal`] = sub(s["future-personal"], s.current);
    row[`gap.${d.key}.stance`] = sub(s["future-team"], s["future-personal"]);
  }
  AREAS.forEach((a, i) => {
    PASSES.forEach(p => row[`area.${a}.${p}`] = area[i][p] ?? "NA");
    row[`area-gap.${a}.personal`] = sub(area[i]["future-personal"], area[i].current);
    row[`area-gap.${a}.stance`] = sub(area[i]["future-team"], area[i]["future-personal"]);
  });
  PROBES.forEach(p => { const [me, team] = P.probes[p]; row[`edge.${p}.future-personal`] = me >= 4 ? 1 : 0; row[`edge.${p}.future-team`] = team >= 4 ? 1 : 0; });
  const S = { current: P.safe.cur, "future-personal": P.safe.fp, "future-team": P.safe.ft };
  SAFEGUARDS.forEach((s, i) => PASSES.forEach(p => row[`safeguard.${s}.${p}`] = S[p].includes(i) ? 1 : 0));
  const inc = list => list.includes(0) && list.length > 1;
  const incCur = inc(P.safe.cur), incFp = inc(P.safe.fp), incFt = inc(P.safe.ft);
  SAFEGUARDS.slice(1).forEach((s, j) => { const i = j + 1;
    row[`lever.${s}`] = (incCur || incFp) ? "NA" : (P.safe.fp.includes(i) && !P.safe.cur.includes(i) ? 1 : 0);
    row[`learn.${s}`] = P.safe.learn.includes(i) ? 1 : 0;
    row[`interest.${s}`] = (P.safe.learn.includes(i) && !P.safe.fp.includes(i)) ? 1 : 0; });
  row["flag.malformed"] = P.blank ? P.blank : 0;
  row["flag.inconsistent-current"] = incCur ? 1 : 0; row["flag.inconsistent-future-personal"] = incFp ? 1 : 0; row["flag.inconsistent-future-team"] = incFt ? 1 : 0;
  row["flag.hold"] = (P.safe.fp.includes(0) && !incFp) ? 1 : 0;
  // #20 Pattern flags — raw answers, before reverse-keying. A block = its answered rows.
  // rows = every answered row of the block (incl. reversed items and probes) · rev = its reverse-keyed rows · plain = the rest
  const block = (ids, pass, probeIdx) => {
    const rows = [...ids.map(f => item[f][pass]), ...(probeIdx == null ? [] : PROBES.map(p => P.probes[p][probeIdx]))];
    const rev = ids.filter(f => REV.has(f)).map(f => item[f][pass]);
    const plain = [...ids.filter(f => !REV.has(f)).map(f => item[f][pass]), ...(probeIdx == null ? [] : PROBES.map(p => P.probes[p][probeIdx]))];
    return { rows, rev, plain };
  };
  const blocks = { current: block(ATTITUDE, "current", null), "future-personal": block(FUT_ITEMS, "future-personal", 0), "future-team": block(FUT_ITEMS, "future-team", 1) };
  const countIf = (xs, v) => xs.filter(x => x === v).length;
  for (const p of PASSES) {
    const rows = blocks[p].rows.filter(x => x != null), rev = blocks[p].rev.filter(x => x != null);
    const share = Math.max(...[1, 2, 3, 4, 5].map(v => countIf(rows, v))) / rows.length;                       // modal share of the WHOLE block (sees the midpoint case)
    // Mode of the NON-reversed rows — what the person says when not reversed. (Taking the mode over the whole block lets
    // a genuine "mostly 4" person's reversed rows at 2 *become* the mode and then trivially agree with it.)
    const plain = blocks[p].plain.filter(x => x != null);
    const topP = Math.max(...[1, 2, 3, 4, 5].map(v => countIf(plain, v)));
    const modes = [1, 2, 3, 4, 5].filter(v => countIf(plain, v) === topP);
    // Reversed rows answered at that mode. Not evidence at the midpoint (6 − 3 = 3: a genuine moderate answers the reversed
    // rows at 3 too), so 3 is skipped when tied with another value; ties → the tied mode with the SMALLER agreement (conservative).
    const cands = modes.length > 1 ? modes.filter(v => v !== 3) : modes;
    const mode = cands.sort((a, b) => countIf(rev, a) - countIf(rev, b))[0];
    const agree = countIf(rev, mode);
    row[`pattern.mode.${p}`] = mode;
    row[`pattern.modal-share.${p}`] = Number(share.toFixed(4));
    row[`pattern.reverse-agree.${p}`] = agree;
    row[`flag.flat-${p}`] = ((mode !== 3 && agree >= rev.length - THRESH.reverseSlack) || share >= THRESH.modalShare) ? 1 : 0;
  }
  const pairs = [...FUT_ITEMS.map(f => [item[f]["future-personal"], item[f]["future-team"]]), ...PROBES.map(p => P.probes[p])].filter(([a, b]) => a != null && b != null);
  row["pattern.stance-identical"] = pairs.filter(([a, b]) => a === b).length;
  row["flag.stance-identical"] = row["pattern.stance-identical"] >= THRESH.stanceIdentical ? 1 : 0;
  for (const d of DIMS) { for (const f of d.cur.flat()) row[`item.${f}.current`] = item[f].current ?? ""; for (const f of d.fut) { row[`item.${f}.future-personal`] = item[f]["future-personal"]; row[`item.${f}.future-team`] = item[f]["future-team"]; } }
  PROBES.forEach(p => { row[`probe.${p}.future-personal`] = P.probes[p][0]; row[`probe.${p}.future-team`] = P.probes[p][1]; });
  return row;
});

const csvCell = v => { const s = String(v); return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
const csv = [header.join(","), ...rows.map(row => header.map(h => { if (!(h in row)) throw new Error(`missing ${h}`); return csvCell(row[h]); }).join(","))].join("\r\n") + "\r\n";
writeFileSync(OUT, "﻿" + csv, "utf8"); // BOM, as Excel's "CSV UTF-8" writes it — the loader must strip it
console.log(`${OUT}: ${rows.length} rows × ${header.length} columns`);
