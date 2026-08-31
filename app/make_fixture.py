"""Regenerate app/sample-export.xlsx — the committed, fully FAKE Forms export fixture.

Decided in #27: the repo never holds real survey data; dev and tests run against
this file. v2 (#34): the header is synthesized from survey/SURVEY.md via
serve.py's survey map — no real v2 export exists to copy from — and 7 invented
respondents get deterministic, persona-shaded answers so the dashboard has
spread, gaps and a few N/As to show. Re-run when the survey's wording changes:

    python app/make_fixture.py
"""
import random, sys, zipfile
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from serve import SURVEY, SCALES, survey_header

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "app" / "sample-export.xlsx"
FAKE = [("Ada Fixture", "ada@example.invalid", 0.80), ("Bo Sample", "bo@example.invalid", 0.35),
        ("Cy Mock", "cy@example.invalid", 0.90), ("Dee Stub", "dee@example.invalid", 0.15),
        ("Ed Dummy", "ed@example.invalid", 0.55), ("Fay Test", "fay@example.invalid", 0.70),
        ("Gus Fake", "gus@example.invalid", 0.30)]     # persona: appetite for AI, 0..1

def pick_level(rng, k, persona):
    """A plausible answer: persona-centred gaussian, clamped to 1..k."""
    return max(1, min(k, round(rng.gauss(1 + (k - 1) * persona, 1.1))))

def fake_cells(name, persona):
    cells = {}
    for q in SURVEY:
        if q["choice"]:
            opts = [t for _, t in q["items"]]
            rng = random.Random(f"{name}|Q{q['num']}")
            picked = [o for o in opts if rng.random() < 0.25 + 0.3 * persona]
            if not picked and q["num"] != 11:
                picked = [opts[int(persona * 7)]]
            if q["num"] == 11 and rng.random() < 0.3:
                picked = []                            # know-more is the one optional question
            if picked:
                cells[q["title"]] = "; ".join(picked)
            continue
        labels = SCALES[q["scale"]]
        for iid, stmt in q["items"]:
            rng = random.Random(f"{name}|{iid}")
            if q["scale"] == "Involvement":
                # N/A hangs off the AREA, so the two passes mostly pair (spec §4)
                area = iid.rsplit(".", 2)[1]
                na = random.Random(f"{name}|na|{area}").random()
                if na < 0.06 or (na < 0.09 and iid.endswith(".current")):
                    cells[stmt] = labels[-1]           # N/A – I don't do this work
                    continue
                lean = persona + (0.12 if iid.endswith(".direction") else 0)
                cells[stmt] = labels[pick_level(rng, len(labels) - 1, lean) - 1]
            else:
                lean = persona + (0.12 if q["num"] in (7, 9) else 0)   # direction runs warmer
                cells[stmt] = labels[pick_level(rng, len(labels), min(1, lean)) - 1]
    return cells

def col_ref(i):
    s = ""
    i += 1
    while i: i, r = divmod(i - 1, 26); s = chr(65 + r) + s
    return s

def write_xlsx(header, rows, out):
    strings, index = [], {}
    def sid(s):
        if s not in index: index[s] = len(strings); strings.append(s)
        return index[s]
    def row_xml(rn, vals):
        cells = []
        for i, v in enumerate(vals):
            if v is None: continue
            ref = f"{col_ref(i)}{rn}"
            if isinstance(v, (int, float)): cells.append(f'<c r="{ref}"><v>{v}</v></c>')
            else: cells.append(f'<c r="{ref}" t="s"><v>{sid(v)}</v></c>')
        return f'<row r="{rn}">{"".join(cells)}</row>'
    body = [row_xml(1, header)]
    for n, r in enumerate(rows): body.append(row_xml(n + 2, r))
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
             f'<sheetData>{"".join(body)}</sheetData></worksheet>')
    ss = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{len(strings)}" uniqueCount="{len(strings)}">'
          + "".join(f"<si><t xml:space=\"preserve\">{escape(s)}</t></si>" for s in strings) + "</sst>")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            '<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>'
            '</Types>')
        z.writestr("_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '</Relationships>')
        z.writestr("xl/workbook.xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<sheets><sheet name="Sheet1" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/>'
            '</Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", sheet)
        z.writestr("xl/sharedStrings.xml", ss)

def main():
    header = survey_header()
    out_rows = []
    for n, (name, email, persona) in enumerate(FAKE):
        cells = fake_cells(name, persona)
        cells.update({"ID": n + 1, "Start time": 46200.5 + n, "Completion time": 46200.52 + n,
                      "Email": email, "Name": name})
        out_rows.append([cells.get(h) for h in header])
    write_xlsx(header, out_rows, OUT)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out_rows)} fake respondents x {len(header)} columns"
          f" (header synthesized from survey/SURVEY.md)")

if __name__ == "__main__":
    main()
