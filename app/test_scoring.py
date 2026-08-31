"""Tests for serve.py's score() — run:  python -m unittest discover app

The main case is Sofia Marchetti, the fictional worked example in
rubric/RUBRIC.md §8, handed to #34 as a ready-made test: every expected number
below is computed by hand in that file. Her row is built through the same
survey map serve.py uses, so wording changes in SURVEY.md don't break the test.
"""
import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import serve
from serve import SCALES, STMT, CHOICE_TITLE, SAFEGUARDS, SURVEY, survey_header, score

def label(scale, v):
    return SCALES[scale][v - 1]

NA = SCALES["Involvement"][-1]           # "N/A – I don't do this work"
SCALE_OF = {iid: q["scale"] for q in SURVEY if not q["choice"] for iid, _ in q["items"]}

def likert(row, iid, v):
    row[STMT[iid]] = label(SCALE_OF[iid], v)

def safeguard_cell(row, asking, keys):
    row[CHOICE_TITLE[asking]] = "; ".join(t for k, t in SAFEGUARDS if k in keys)

# Sofia's answers, straight from RUBRIC.md §8.1 (raw, before reverse-keying)
SOFIA_CURRENT = dict(C1=3, C2=2, C3=4, T1=2, T2=3, T3=2, F1=2, F2=3, F3=4,
                     G1=3, G2=3, G3=3, G4=3, G5=4, G6=2,
                     N1=3, N2=3, N3=4, N4=3, N5=4, A1=2, A2=4, A3=2,
                     V1=3, V2=3, V3=4)
SOFIA_DIRECTION = {"D-C1": 4, "D-C2": 2, "D-T1": 4, "D-T2": 2, "D-F1": 4, "D-F2": 1,
                   "D-G1": 3, "D-G2": 3, "D-G3": 3, "D-G4": 3, "D-G5": 3,
                   "D-N1": 2, "D-N2": 3, "D-N3": 3, "D-N4": 3, "D-N5": 3,
                   "D-A1": 4, "D-A2": 2, "D-V1": 3, "D-V2": 3,
                   "P1": 2, "P2": 3, "P3": 3, "P4": 2, "P5": 3}
SOFIA_COVERAGE = {  # area key: (today, direction); None = N/A
    "requirements": (4, 6), "tests": (2, 3), "code-review": (2, 3),
    "infrastructure": (None, None), "security-review": (None, 3),
    "estimates": (3, 5), "meeting-notes": (3, 5)}

def sofia_row():
    row = {"Name": "Sofia Marchetti", "Email": "sofia@example.invalid"}
    for iid, v in {**SOFIA_CURRENT, **SOFIA_DIRECTION}.items():
        likert(row, iid, v)
    for akey, _ in serve.AREAS:
        cur, dr = SOFIA_COVERAGE.get(akey, (3, 3))
        row[STMT[f"area.{akey}.current"]] = NA if cur is None else label("Involvement", cur)
        row[STMT[f"area.{akey}.direction"]] = NA if dr is None else label("Involvement", dr)
    safeguard_cell(row, "today", {"another-person"})
    safeguard_cell(row, "willing", {"read-all", "tests"})
    safeguard_cell(row, "team", {"another-person"})   # not in §8.1; any answer works
    row[CHOICE_TITLE["learn"]] = "; ".join(t for k, t in SAFEGUARDS
                                           if k in {"schema-check", "small-blast-radius"})
    for iid in serve.block_ids("Agreement"):     # team: flat 3s (v1 Sofia has no team row)
        likert(row, iid, 3)
    for iid, _ in next(q for q in SURVEY if q["num"] == 1)["items"]:
        row[STMT[iid]] = label("Tool use", 3)
    return row

def one(rows):
    return score(survey_header(), rows)["people"]

class SofiaScores(unittest.TestCase):
    def setUp(self):
        self.p = one([sofia_row()])[0]

    def assertScores(self, fam, expected):
        for key, want in expected.items():
            self.assertAlmostEqual(self.p[fam][key], want, places=2, msg=f"{fam}.{key}")

    def test_current(self):
        self.assertScores("current", {
            "comfort": 2.33, "trust": 2.33, "fluency": 2.33, "guardrails": 3.40,
            "concern": 3.40, "autonomy": 2.00, "craft-values": 3.33})

    def test_direction(self):
        self.assertScores("direction", {
            "comfort": 4.00, "trust": 4.00, "fluency": 4.50, "guardrails": 3.00,
            "concern": 2.80, "autonomy": 4.00, "craft-values": 3.00})

    def test_gap(self):
        self.assertScores("gap", {
            "comfort": 1.67, "trust": 1.67, "fluency": 2.17, "guardrails": -0.40,
            "concern": -0.60, "autonomy": 2.00, "craft-values": -0.33})

    def test_coverage(self):
        cov = self.p["cov"]
        self.assertEqual(cov["requirements"]["gap"], 2)
        self.assertEqual(cov["infrastructure"]["pairing"], "both-na")
        self.assertIsNone(cov["infrastructure"]["gap"])
        self.assertEqual(cov["security-review"]["pairing"], "today-na")   # flagged, no Gap
        self.assertIsNone(cov["security-review"]["gap"])

    def test_edges(self):
        # Requirements at 6 raises nothing (not high-stakes); no probe at 4-5
        self.assertEqual(self.p["edges_coverage"], [])
        self.assertEqual(self.p["edges_probes"], [])

    def test_safeguards(self):
        self.assertEqual(self.p["levers"], {"read-all", "tests"})
        self.assertEqual(self.p["dropped"], {"another-person"})
        self.assertEqual(self.p["holds"], set())

    def test_team_flat_3(self):
        for key, _ in serve.TEAM_DIMS:
            self.assertAlmostEqual(self.p["norm"][key], 3.0, msg=key)
        self.assertAlmostEqual(self.p["facet"]["Parallel development"], 3.0)
        self.assertAlmostEqual(self.p["facet"]["Limits"], 3.0)

    def test_flags(self):
        self.assertFalse(self.p["flags"]["current"]["flag"])    # varied answers
        self.assertFalse(self.p["flags"]["direction"]["flag"])
        # flat 3s: mode 3 gives no reverse-key evidence, but modal share 24/24 flags
        self.assertTrue(self.p["flags"]["team"]["flag"])
        self.assertEqual(self.p["flags"]["team"]["share"], 1.0)
        self.assertEqual(self.p["flags"]["current"]["mode"], 3)
        self.assertNotIn("malformed", {m for m in self.p["malformed"]})

    def test_nothing_malformed(self):
        self.assertEqual(self.p["malformed"], [])

class StraightLiner(unittest.TestCase):
    def test_flat_4_current_block_flags(self):
        row = sofia_row()
        for iid in serve.block_ids("Attitude"):
            likert(row, iid, 4)
        p = one([row])[0]
        f = p["flags"]["current"]
        self.assertEqual(f["mode"], 4)
        self.assertEqual(f["agreement"], 5)      # all 5 reversed rows answered at the mode
        self.assertTrue(f["flag"])

class Malformed(unittest.TestCase):
    def test_blank_scored_answer_is_na_not_data(self):
        row = sofia_row()
        del row[STMT["C1"]]
        p = one([row])[0]
        self.assertIsNone(p["current"]["comfort"])          # reads #N/A, not averaged around
        self.assertIsNotNone(p["current"]["trust"])
        self.assertIn("C1", p["malformed"])

class CurlyQuotes(unittest.TestCase):
    def test_forms_curled_apostrophes_still_match(self):
        row = sofia_row()
        curled = {k.replace("'", "’"): v for k, v in row.items()}
        header = [h.replace("'", "’") for h in survey_header()]
        p = score(header, [curled])["people"][0]
        self.assertAlmostEqual(p["current"]["comfort"], 2.33, places=2)
        self.assertEqual(p["malformed"], [])

class Fixture(unittest.TestCase):
    def test_fixture_parses_and_scores(self):
        path = Path(__file__).resolve().parent / "sample-export.xlsx"
        if not path.is_file():
            self.skipTest("fixture not built yet (python app/make_fixture.py)")
        header, rows = serve.parse_export(path)
        result = score(header, rows)
        self.assertEqual(result["missing"], [])
        view = serve.team_view(result, path.name, True)
        self.assertEqual(view["n"], len(rows))
        self.assertEqual(len(view["q1"]), 7)
        self.assertEqual(len(view["q3"]), 19)
        self.assertEqual(sum(len(g["items"]) for g in view["q5"]), 24)
        serve.render_csv(result)                 # renders without error

if __name__ == "__main__":
    unittest.main()
