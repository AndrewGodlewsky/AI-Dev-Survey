"""The v2 app (wayfinder #26 architecture, #34 build).

Drop the raw Forms .xlsx in data/  ->  python app/serve.py  ->  dashboard on localhost.

- Items map: parsed from survey/SURVEY.md at startup. Item text is the database
  key; wording changes go in that file first and only there.
- Scoring: implements scoring/scoring-rules-v2.md (#28) in score().
- Seam: Python computes, the browser draws. dashboard/dashboard.html is served
  at "/" and fetches /scored.json; /scored.csv is the on-demand export (§7).
- Stdlib only, on purpose: any Python 3, no venv, no pip install. XML safety:
  DTDs are rejected before parsing (a Forms export never carries one).
"""
import json, re, sys, webbrowser, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PORT = 8737
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
BUILTINS = ["ID", "Start time", "Completion time", "Email", "Name", "Last modified time"]

def fail(msg):
    print(f"\n  problem: {msg}\n", file=sys.stderr)
    sys.exit(1)

# ---- 1. the survey map (from survey/SURVEY.md — the verbatim form) ----------

def norm_text(s):
    """Matching form of a statement/option: Forms curls quotes; the doc decorates
    with markdown. Both sides of every header/cell match go through this."""
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("`", "").replace("*", "")
    return " ".join(s.split())

def load_survey():
    """Every '### Qn' block: title, scale, and the | # | ID | text | table rows.
    Also the six scale label sets from the 'The scales' table."""
    text = (ROOT / "survey" / "SURVEY.md").read_text(encoding="utf-8")
    questions, scales, q = [], {}, None
    for line in text.splitlines():
        m = re.match(r"### Q(\d+) · (\w+)", line)
        if m:
            q = {"num": int(m.group(1)), "choice": m.group(2) == "Choice",
                 "title": None, "scale": None, "items": []}
            questions.append(q)
            continue
        m = re.match(r"\| \*\*(.+?)\*\* \| (`\d.+`)", line)   # scales table rows
        if m:
            scales[m.group(1)] = re.findall(r"`([^`]+)`", m.group(2))
            continue
        if q:
            m = re.match(r"\*\*Title:\*\* `(.+)`", line)
            if m: q["title"] = m.group(1)
            m = re.match(r"\*\*Scale:\*\* ([\w ]+?) \(", line)
            if m: q["scale"] = m.group(1)
            m = re.match(r"\| *\d+ *\| *(\S+) *\| *(.+?) *\|$", line)
            if m: q["items"].append((m.group(1), m.group(2).replace("`", "").replace("*", "")))
    if len(questions) != 14:
        fail(f"survey/SURVEY.md parse found {len(questions)} questions, expected 14")
    return questions, scales

SURVEY, SCALES = load_survey()
STMT = {iid: stmt for q in SURVEY if not q["choice"] for iid, stmt in q["items"]}
CHOICE_TITLE = {  # asking -> the Forms question title (= the export column header)
    "today": next(q["title"] for q in SURVEY if q["num"] == 6),
    "willing": next(q["title"] for q in SURVEY if q["num"] == 10),
    "learn": next(q["title"] for q in SURVEY if q["num"] == 11),
    "team": next(q["title"] for q in SURVEY if q["num"] == 14),
}
SAFEGUARDS = [(iid.split(".")[1], text)                       # (key, option text), in order
              for iid, text in next(q for q in SURVEY if q["num"] == 6)["items"]]
AREAS = [(iid.split(".")[1], stmt.split(": ", 1)[1])          # (key, label), grid order
         for iid, stmt in next(q for q in SURVEY if q["num"] == 3)["items"]]

def survey_header():
    """The column headers a v2 Forms export carries, in form order (fixture + tests)."""
    cols = list(BUILTINS)
    for q in SURVEY:
        cols += [q["title"]] if q["choice"] else [stmt for _, stmt in q["items"]]
    return cols

# ---- 2. the scoring spec (scoring/scoring-rules-v2.md) ----------------------

REVERSE = {"C3", "T2", "F3", "G6", "N4", "A2", "V2",
           "D-C2", "D-T2", "D-F2", "D-G5", "D-N4", "D-A2", "D-V2",
           "TR3", "TR6", "VE3", "AL3", "AL4", "AL6", "PA2", "SP3", "SP6"}

DIMS = [("comfort", "Comfort"), ("trust", "Trust"), ("fluency", "Fluency"),
        ("guardrails", "Guardrails"), ("concern", "Concern"),
        ("autonomy", "Autonomy"), ("craft-values", "Craft values")]
CURRENT_FACETS = {
    "comfort": [["C1"], ["C2"], ["C3"]], "trust": [["T1"], ["T2"], ["T3"]],
    "fluency": [["F1"], ["F2"], ["F3"]],
    "guardrails": [["G1"], ["G2", "G3"], ["G4"], ["G5"], ["G6"]],   # disclosure collapse
    "concern": [["N1"], ["N2"], ["N3"], ["N4"], ["N5"]],
    "autonomy": [["A1"], ["A2"], ["A3"]], "craft-values": [["V1"], ["V2"], ["V3"]]}
DIRECTION_FACETS = {
    "comfort": [["D-C1"], ["D-C2"]], "trust": [["D-T1"], ["D-T2"]],
    "fluency": [["D-F1"], ["D-F2"]],
    "guardrails": [["D-G1"], ["D-G2"], ["D-G3"], ["D-G4"], ["D-G5"]],
    "concern": [["D-N1"], ["D-N2"], ["D-N3"], ["D-N4"], ["D-N5"]],
    "autonomy": [["D-A1"], ["D-A2"]], "craft-values": [["D-V1"], ["D-V2"]]}

TEAM_DIMS = [("transparency", "Transparency"), ("verification", "Verification"),
             ("agent-latitude", "Agent latitude"), ("pace", "Pace"),
             ("shared-practice", "Shared practice")]
TEAM_FACETS = {
    "transparency": [("Disclosure & provenance", ["TR1", "TR2", "TR3"]),
                     ("Ownership & accountability", ["TR4", "TR5", "TR6"])],
    "verification": [("Reviewing AI-assisted work", ["VE1", "VE2", "VE3"])],
    "agent-latitude": [("Parallel development", ["AL1", "AL2", "AL3"]),
                       ("Limits", ["AL4", "AL5", "AL6"])],
    "pace": [("Pace & risk appetite", ["PA1", "PA2", "PA3"])],
    "shared-practice": [("Shared conventions & tooling", ["SP1", "SP2", "SP3"]),
                        ("Learning & skill", ["SP4", "SP5", "SP6"])]}

PROBES = ["P1", "P2", "P3", "P4", "P5"]
HIGH_STAKES = {"security-review", "incident-response", "code-review",
               "data-migrations", "infrastructure", "ci-cd"}
READING_POSITIONS = {"read-all", "another-person", "read-risky"}

# Pattern-flag blocks (§6): identified by scale; thresholds tunable after the pilot.
FLAG_BLOCKS = [("current", "Attitude"), ("direction", "Desirability"), ("team", "Agreement")]
FLAG_AGREEMENT_SLACK = 1      # flag when agreement >= reversed rows answered - this
FLAG_MODAL_SHARE = 0.90       # or when one answer is >= this share of the block

def block_ids(scale):
    return [iid for q in SURVEY if q["scale"] == scale for iid, _ in q["items"]]

# ---- 3. find + parse the export (stdlib zip + XML) --------------------------

def find_export(argv):
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) > 1:
        p = Path(argv[1])
        if not p.is_file(): fail(f"no file at {p}")
        return p, p.resolve() == (ROOT / "app" / "sample-export.xlsx")
    DATA.mkdir(exist_ok=True)
    files = sorted(DATA.glob("*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        fixture = ROOT / "app" / "sample-export.xlsx"
        if fixture.is_file():
            print("  data/ is empty - falling back to the committed FAKE fixture (app/sample-export.xlsx).")
            return fixture, True
        fail(f"no .xlsx found. Drop the raw Forms export into {DATA} and run again.")
    if len(files) > 1:
        print(f"  {len(files)} .xlsx files in data/ - using the newest, ignoring: "
              + ", ".join(p.name for p in files[1:]))
    return files[0], False

def cell_ref_to_col(ref):
    n = 0
    for ch in ref:
        if ch.isdigit(): break
        n = n * 26 + ord(ch) - 64
    return n - 1

def parse_export(path):
    try:
        z = zipfile.ZipFile(path)
        for part in ("xl/sharedStrings.xml", "xl/worksheets/sheet1.xml"):
            if b"<!DOCTYPE" in z.read(part)[:1024]:
                fail(f"{path.name} contains a DTD - not a Forms export.")
        shared = ["".join(t.text or "" for t in si.findall(".//m:t", NS))
                  for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS)]
        sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as e:
        fail(f"{path.name} is not a readable Forms export ({e}). Re-download it from Forms.")
    def val(c):
        v = c.findtext("m:v", None, NS)
        if v is None: return None
        return shared[int(v)] if c.get("t") == "s" else v
    grid = []
    for row in sheet.findall(".//m:row", NS):
        cells = {}
        for c in row.findall("m:c", NS):
            cells[cell_ref_to_col(c.get("r"))] = val(c)
        grid.append(cells)
    if len(grid) < 2:
        fail(f"{path.name} has a header but no responses.")
    width = max(max(r) for r in grid if r) + 1
    header = [grid[0].get(i) for i in range(width)]
    rows = [{header[i]: r.get(i) for i in range(width) if header[i]} for r in grid[1:]]
    return header, rows

def label_num(label):
    """Forms exports label text; scored labels lead with their digit ('5 – Always')."""
    if label is None: return None
    m = re.match(r"\s*(\d+)\b", str(label))
    return int(m.group(1)) if m else None   # None: N/A, checklists, free text

# ---- 4. score (scoring/scoring-rules-v2.md) ---------------------------------

def mean(vals): return sum(vals) / len(vals)
def r4(x): return None if x is None else round(x, 4)

def low_median(vals):
    """Ordinal median; even n takes the LOWER middle (spec §4)."""
    if not vals: return None
    s = sorted(vals)
    return s[(len(s) - 1) // 2]

def initials_for(names):
    """#27: initials everywhere, surname-extension on collisions, full name on hover."""
    def take(n, k):
        p = [x for x in n.split() if x] or ["?"]
        first, last = p[0], (p[-1] if len(p) > 1 else p[0][1:] or "?")
        return first[0].upper() + last[:k].capitalize()
    ks, out = [1] * len(names), [take(n, 1) for n in names]
    for _ in range(8):
        dup = {s for s in out if out.count(s) > 1}
        if not dup: break
        for i, s in enumerate(out):
            if s in dup:
                ks[i] += 1
                out[i] = take(names[i], ks[i])
    seen = set()
    for i in range(len(out)):                   # identical names: last-resort tick
        while out[i] in seen: out[i] += "'"
        seen.add(out[i])
    return out

def score(header, rows):
    """Raw parsed export -> per-Respondent computed values (the CSV's row, §7)."""
    lookup = {norm_text(h): h for h in header if h}
    missing = [iid for iid, stmt in STMT.items() if norm_text(stmt) not in lookup]
    missing += [f"choice:{a}" for a, t in CHOICE_TITLE.items()
                if a != "learn" and norm_text(t) not in lookup]

    def get(row, iid):
        h = lookup.get(norm_text(STMT[iid]))
        return row.get(h) if h else None
    def raw(row, iid):
        return label_num(get(row, iid))
    def keyed(row, iid):
        n = raw(row, iid)
        return None if n is None else (6 - n if iid in REVERSE else n)
    def facet_mean(row, facets):
        vals, bad = [], []
        for facet in facets:
            fv = [keyed(row, i) for i in facet]
            bad += [i for i, v in zip(facet, fv) if v is None]
            vals.append(None if None in fv else mean(fv))
        return (None, bad) if bad else (mean(vals), [])
    def choice_cell(row, asking):
        h = lookup.get(norm_text(CHOICE_TITLE[asking]))
        return row.get(h) if h else None
    def ticks(row, asking):
        cell = choice_cell(row, asking)
        if not cell: return set()
        c = norm_text(cell)
        return {key for key, text in SAFEGUARDS if norm_text(text) in c}

    names = [r.get("Name") or f"Respondent {i + 1}" for i, r in enumerate(rows)]
    people = []
    for row, name, ini in zip(rows, names, initials_for(names)):
        p = {"name": name, "initials": ini, "malformed": []}
        for fam, facets in (("current", CURRENT_FACETS), ("direction", DIRECTION_FACETS)):
            p[fam] = {}
            for key, _ in DIMS:
                v, bad = facet_mean(row, facets[key])
                p[fam][key] = v
                p["malformed"] += bad
        p["gap"] = {key: (None if p["current"][key] is None or p["direction"][key] is None
                          else p["direction"][key] - p["current"][key]) for key, _ in DIMS}
        p["norm"], p["facet"] = {}, {}
        for key, _ in TEAM_DIMS:
            v, bad = facet_mean(row, [ids for _, ids in TEAM_FACETS[key]])
            p["norm"][key] = v
            p["malformed"] += bad
            for flabel, ids in TEAM_FACETS[key]:
                fv = [keyed(row, i) for i in ids]
                p["facet"][flabel] = None if None in fv else mean(fv)
        # §3.2: raw team answers, before reverse-keying — what the norms chart counts
        p["team_raw"] = {iid: raw(row, iid) for iid in block_ids("Agreement")}
        # Coverage: raw Involvement levels, never averaged (§4)
        p["cov"] = {}
        for akey, _ in AREAS:
            lv = {}
            for pas in ("current", "direction"):
                cell = get(row, f"area.{akey}.{pas}")
                if cell is None:
                    lv[pas] = None
                    p["malformed"].append(f"area.{akey}.{pas}")
                else:
                    lv[pas] = label_num(cell) or "NA"
            both = all(isinstance(lv[x], int) for x in ("current", "direction"))
            lv["gap"] = lv["direction"] - lv["current"] if both else None
            lv["pairing"] = ("ok" if both else
                             "both-na" if lv["current"] == "NA" and lv["direction"] == "NA" else
                             "today-na" if lv["current"] == "NA" else
                             "direction-na" if lv["direction"] == "NA" else "blank")
            p["cov"][akey] = lv
        # Edge markers (§5): level 6 on a high-stakes area, per pass, labelled; probes at 4-5
        p["edges_coverage"] = [f"{'today' if pas == 'current' else pas}: {label}"
                               for akey, label in AREAS if akey in HIGH_STAKES
                               for pas in ("current", "direction") if p["cov"][akey][pas] == 6]
        p["edges_probes"] = [pr for pr in PROBES if (raw(row, pr) or 0) >= 4]
        # Safeguards: three askings, one symmetric list; Levers/Holds/Dropped by subtraction
        for asking in ("today", "willing", "team"):
            p[f"safeguard_{asking}"] = ticks(row, asking)
            if choice_cell(row, asking) is None:
                p["malformed"].append(f"safeguard:{asking}")
        p["levers"] = p["safeguard_willing"] - p["safeguard_today"]
        p["holds"] = p["safeguard_willing"] & p["safeguard_today"] & READING_POSITIONS
        p["dropped"] = p["safeguard_today"] - p["safeguard_willing"]
        # Pattern flags (§6): raw answers, blanks excluded
        p["flags"] = {}
        for block, scale in FLAG_BLOCKS:
            answered = {i: v for i in block_ids(scale) if (v := raw(row, i)) is not None}
            plain = [v for i, v in answered.items() if i not in REVERSE]
            rev = [v for i, v in answered.items() if i in REVERSE]
            if not plain:
                p["flags"][block] = {"flag": False, "mode": None, "share": None, "agreement": None}
                continue
            top = max(map(plain.count, set(plain)))
            cand = sorted(v for v in set(plain) if plain.count(v) == top)
            if len(cand) > 1: cand = [v for v in cand if v != 3] or cand
            mode = min(cand, key=lambda v: rev.count(v))          # tie: smaller agreement
            agreement = rev.count(mode)
            allv = list(answered.values())
            share = max(map(allv.count, set(allv))) / len(allv)
            p["flags"][block] = {
                "mode": mode, "share": r4(share), "agreement": agreement,
                "flag": (mode != 3 and agreement >= len(rev) - FLAG_AGREEMENT_SLACK)
                        or share >= FLAG_MODAL_SHARE}
        p["malformed"] = sorted(set(p["malformed"]))
        people.append(p)
    return {"people": people, "missing": sorted(set(missing))}

# ---- 5. team level + the five questions -------------------------------------

def present(vals): return [v for v in vals if v is not None]

def agg(vals):
    """Team score: mean + range + every value, with its own n. No stdev (§1.5)."""
    vs = present(vals)
    return {"values": [r4(v) for v in vals],
            "mean": r4(mean(vs)) if vs else None,
            "range": r4(max(vs) - min(vs)) if vs else None, "n": len(vs)}

def f1(x): return "?" if x is None else f"{x:.1f}"

def team_view(result, src_name, fixture):
    """Everything dashboard.html draws, computed here — the browser only renders."""
    ppl = result["people"]
    q1 = []
    for key, label in DIMS:
        a = agg([p["current"][key] for p in ppl])
        a.update(key=key, label=label)
        q1.append(a)
    q2 = []
    for key, label in DIMS:
        cur = agg([p["current"][key] for p in ppl])
        dr = agg([p["direction"][key] for p in ppl])
        gap = None if cur["mean"] is None or dr["mean"] is None else r4(dr["mean"] - cur["mean"])
        q2.append({"key": key, "label": label, "gap": gap,
                   "mean_cur": cur["mean"], "mean_dir": dr["mean"]})
    q2.sort(key=lambda o: -(o["gap"] if o["gap"] is not None else -99))
    q3 = []
    for akey, label in AREAS:
        cur = [p["cov"][akey]["current"] for p in ppl if isinstance(p["cov"][akey]["current"], int)]
        dr = [p["cov"][akey]["direction"] for p in ppl if isinstance(p["cov"][akey]["direction"], int)]
        moves = [p["cov"][akey]["gap"] for p in ppl if p["cov"][akey]["gap"] is not None]
        q3.append({"key": akey, "label": label,
                   "cur_med": low_median(cur), "dir_med": low_median(dr),
                   "move_med": low_median(moves), "n_moves": len(moves),
                   "n": {"cur": len(cur), "dir": len(dr)},
                   "na": {"cur": sum(1 for p in ppl if p["cov"][akey]["current"] == "NA"),
                          "dir": sum(1 for p in ppl if p["cov"][akey]["direction"] == "NA")}})
    q3.sort(key=lambda o: (-(o["move_med"] if o["move_med"] is not None else -99), o["label"]))
    q4 = [{"label": o["label"], "values": o["values"], "range": o["range"]}
          for o in sorted((o for o in q1 if o["n"] >= 2), key=lambda o: -o["range"])[:4]]
    q5 = []
    for key, label in TEAM_DIMS:
        items = []
        for flabel, ids in TEAM_FACETS[key]:
            for iid in ids:
                counts = [0] * 5      # §3.2 raw counts per level — never binned scores
                for p in ppl:
                    v = p["team_raw"].get(iid)
                    if v: counts[v - 1] += 1
                items.append({"id": iid, "facet": flabel, "text": STMT[iid],
                              "rev": iid in REVERSE, "counts": counts})
        facets = [{"label": fl, "mean": r4(m)} for fl, _ in TEAM_FACETS[key]
                  if (m := (mean(present([p["facet"][fl] for p in ppl]))
                            if present([p["facet"][fl] for p in ppl]) else None)) or True]
        q5.append({"key": key, "label": label,
                   "norm": agg([p["norm"][key] for p in ppl]),
                   "facets": facets, "items": items})
    view = {"file": src_name, "fixture": fixture, "n": len(ppl),
            "people": [{"name": p["name"], "initials": p["initials"]} for p in ppl],
            "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5,
            "malformed": [{"name": p["name"], "ids": p["malformed"]}
                          for p in ppl if p["malformed"]],
            "warnings": ([f"{len(result['missing'])} survey column(s) missing from the "
                          f"export (wording drift?): {', '.join(result['missing'][:8])}"
                          + ("…" if len(result["missing"]) > 8 else "")]
                         if result["missing"] else [])}
    view["takes"] = takeaways(view)
    return view

def takeaways(v):
    """One computed sentence per question. Formulaic on purpose — the numbers talk."""
    t = {}
    spread = sorted((o for o in v["q1"] if o["range"] is not None), key=lambda o: -o["range"])
    if spread:
        w = spread[0]
        t["q1"] = (f"Widest spread today: {w['label']} ({w['range']:.1f} between lowest and "
                   f"highest). Tightest: {spread[-1]['label']} ({spread[-1]['range']:.1f})."
                   if w["range"] >= 1.5 else
                   f"No Dimension splits the team by more than {w['range']:.1f} today.")
    pos = [o for o in v["q2"] if o["gap"] is not None and o["gap"] >= 0.3]
    neg = [o for o in v["q2"] if o["gap"] is not None and o["gap"] <= -0.3]
    parts = []
    if pos: parts.append("Appetite for more: " + ", ".join(
        f"{o['label']} (+{o['gap']:.1f})" for o in pos[:3]))
    if neg: parts.append("would pull back: " + ", ".join(
        f"{o['label']} ({o['gap']:.1f})" for o in neg[-3:]))
    t["q2"] = ("Appetite minus practice — never a forecast. "
               + ("; ".join(parts) + "." if parts else
                  "No Dimension moves by 0.3 or more either way."))
    movers = [o for o in v["q3"] if (o["move_med"] or 0) >= 1]
    still = sum(1 for o in v["q3"] if not o["move_med"])
    t["q3"] = ((f"Median moves of a level or more: "
                + ", ".join(o["label"] for o in movers[:4])
                + (f" — and {still} area(s) stay where they are." if still else "."))
               if movers else "No area's median moves a full level.")
    if v["q4"]:
        w = v["q4"][0]
        vals = [x for x in w["values"] if x is not None]
        lo, hi = min(vals), max(vals)
        ppl = v["people"]
        pl = ppl[w["values"].index(lo)]["initials"]
        ph = ppl[w["values"].index(hi)]["initials"]
        t["q4"] = (f"{w['label']} spans {lo:.1f} ({pl}) to {hi:.1f} ({ph}) — "
                   "the widest conversation in the room.")
    div, cons = None, None
    for g in v["q5"]:
        for it in g["items"]:
            c = it["counts"]
            sides = (c[0] + c[1], c[3] + c[4])
            item = (min(sides), sum(c), it, g)
            if div is None or item[0] > div[0]: div = item
            if (cons is None or abs(sides[1] - sides[0]) > cons[0]) and min(sides) == 0:
                cons = (abs(sides[1] - sides[0]), sum(c), it, g)
    if div and div[0] >= 2:
        c = div[2]["counts"]
        t["q5"] = (f"Most divided norm: “{div[2]['text']}” ({c[3]+c[4]} agree, {c[0]+c[1]} "
                   f"disagree). Spread is the finding — these rows are the conversation.")
    elif cons:
        t["q5"] = f"No norm splits the room hard; the clearest consensus: “{cons[2]['text']}”."
    return t

# ---- 6. the CSV export (§7: computed values and flags, no raw answers) ------

def render_csv(result):
    n = len(result["people"])
    cols = ["respondent", "n"]
    cols += [f"current_{k}" for k, _ in DIMS] + [f"direction_{k}" for k, _ in DIMS]
    cols += [f"gap_{k}" for k, _ in DIMS]
    cols += ["latitude_parallel", "latitude_limits"]
    cols += [f"norm_{k}" for k, _ in TEAM_DIMS]
    for a, _ in AREAS:
        cols += [f"cov_{a}_today", f"cov_{a}_direction", f"cov_{a}_gap", f"cov_{a}_pairing"]
    cols += ["edges_coverage", "edges_probes",
             "safeguard_today", "safeguard_willing", "safeguard_team",
             "levers", "holds", "dropped"]
    for block, _ in FLAG_BLOCKS:
        cols += [f"flag_{block}", f"{block}_mode", f"{block}_share", f"{block}_agreement"]
    cols += ["malformed"]

    def num(x): return "#N/A" if x is None else f"{x:.4g}"
    def sg(keys): return "; ".join(k for k, _ in SAFEGUARDS if k in keys)
    lines = [",".join(cols)]
    for p in result["people"]:
        row = [p["name"], str(n)]
        row += [num(p["current"][k]) for k, _ in DIMS]
        row += [num(p["direction"][k]) for k, _ in DIMS]
        row += [num(p["gap"][k]) for k, _ in DIMS]
        row += [num(p["facet"]["Parallel development"]), num(p["facet"]["Limits"])]
        row += [num(p["norm"][k]) for k, _ in TEAM_DIMS]
        for a, _ in AREAS:
            lv = p["cov"][a]
            row += [("#N/A" if lv["current"] is None else str(lv["current"])),
                    ("#N/A" if lv["direction"] is None else str(lv["direction"])),
                    ("" if lv["gap"] is None else str(lv["gap"])), lv["pairing"]]
        row += ["; ".join(p["edges_coverage"]), "; ".join(p["edges_probes"]),
                sg(p["safeguard_today"]), sg(p["safeguard_willing"]), sg(p["safeguard_team"]),
                sg(p["levers"]), sg(p["holds"]), sg(p["dropped"])]
        for block, _ in FLAG_BLOCKS:
            f = p["flags"][block]
            row += [str(f["flag"]).upper(), "" if f["mode"] is None else str(f["mode"]),
                    "" if f["share"] is None else f"{f['share']:.2f}",
                    "" if f["agreement"] is None else str(f["agreement"])]
        row += ["; ".join(p["malformed"])]
        lines.append(",".join('"' + c.replace('"', '""') + '"'
                              if ("," in c or '"' in c) else c for c in row))
    return "\r\n".join(lines) + "\r\n"

# ---- 7. serve ---------------------------------------------------------------

def main():
    src, fixture = find_export(sys.argv)
    header, rows = parse_export(src)
    stmts = [h for h in header if h and h not in BUILTINS]
    result = score(header, rows)
    view = team_view(result, src.name, fixture)

    print(f"\n  export : {src.name}" + ("  (FAKE fixture)" if fixture else ""))
    print(f"  parsed : {len(rows)} respondent(s) "
          f"({', '.join(p['initials'] + ' ' + p['name'] for p in result['people'])})")
    print(f"           {len(header)} columns, {len(stmts)} statements")
    for w in view["warnings"]:
        print(f"  warning: {w}")
    for m in view["malformed"]:
        print(f"  warning: {m['name']} has malformed answers (scores read #N/A): "
              + ", ".join(m["ids"][:6]) + ("…" if len(m["ids"]) > 6 else ""))
    flagged = [p["name"] for p in result["people"]
               if any(f["flag"] for f in p["flags"].values())]
    if flagged:
        print(f"  note   : pattern flag raised for {', '.join(flagged)} — in the CSV export")

    scored_json = json.dumps(view, ensure_ascii=False).encode("utf-8")
    scored_csv = render_csv(result).encode("utf-8-sig")
    template = (ROOT / "dashboard" / "dashboard.html").read_bytes()
    parsed_json = json.dumps({"file": src.name, "respondents": rows},
                             ensure_ascii=False).encode("utf-8")

    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            routes = {
                "/": ("text/html; charset=utf-8", template, None),
                "/scored.json": ("application/json; charset=utf-8", scored_json, None),
                "/scored.csv": ("text/csv; charset=utf-8", scored_csv,
                                'attachment; filename="scored.csv"'),
                "/parsed.json": ("application/json; charset=utf-8", parsed_json, None),
            }
            if self.path == "/favicon.ico":
                self.send_response(204); self.end_headers()
            elif self.path.split("?")[0] in routes:
                ctype, body, dispo = routes[self.path.split("?")[0]]
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                if dispo: self.send_header("Content-Disposition", dispo)
                self.end_headers()
                self.wfile.write(body)
            else:
                self.send_error(404)
        def log_message(self, *a): pass

    url = f"http://localhost:{PORT}/"
    print(f"\n  dashboard: {url}   (CSV export: {url}scored.csv)   Ctrl+C stops it.\n")
    if "--no-browser" not in sys.argv: webbrowser.open(url)
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
    except KeyboardInterrupt:
        print("  stopped.")

if __name__ == "__main__":
    main()
