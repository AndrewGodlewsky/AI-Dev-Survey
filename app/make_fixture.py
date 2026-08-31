"""Regenerate app/sample-export.xlsx — the committed, fully FAKE Forms export fixture.

Decided in #27: the repo never holds real survey data; dev and tests run against
this file. It copies the *header row* (statement text — no personal data) from a
real export and fabricates 7 respondents with invented names/emails and
deterministic answers. Re-run when the survey's columns change (e.g. once #29
assembles v2):  python app/make_fixture.py [path-to-real-export.xlsx]
(default source: newest .xlsx in data/)
"""
import re, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "app" / "sample-export.xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
FAKE = [("Ada Fixture", "ada@example.invalid"), ("Bo Sample", "bo@example.invalid"),
        ("Cy Mock", "cy@example.invalid"), ("Dee Stub", "dee@example.invalid"),
        ("Ed Dummy", "ed@example.invalid"), ("Fay Test", "fay@example.invalid"),
        ("Gus Fake", "gus@example.invalid")]
BUILTINS = ["ID", "Start time", "Completion time", "Email", "Name", "Last modified time"]

def read_export(path):
    z = zipfile.ZipFile(path)
    shared = ["".join(t.text or "" for t in si.findall(".//m:t", NS))
              for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS)]
    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    rows = []
    for row in sheet.findall(".//m:row", NS):
        cells = {}
        for c in row.findall("m:c", NS):
            v = c.findtext("m:v", None, NS)
            col = 0
            for ch in c.get("r"):
                if ch.isdigit(): break
                col = col * 26 + ord(ch) - 64
            cells[col - 1] = shared[int(v)] if (v is not None and c.get("t") == "s") else v
        rows.append(cells)
    width = max(max(r) for r in rows if r) + 1
    return [rows[0].get(i) for i in range(width)], [ [r.get(i) for i in range(width)] for r in rows[1:] ]

def fake_cell(src, person, col):
    """Deterministic fake answer: keep the label's wording, vary its leading digit."""
    if src is None: return None
    m = re.match(r"\s*(\d+)(\D.*)$", src, re.S)
    if not m: return src            # checklist / free-label cells: option text, no digits to vary
    hi = 6 if int(m.group(1)) > 5 else 5
    return f"{(person * 3 + col) % hi + 1}{m.group(2)}"

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
    if len(sys.argv) > 1:
        src = Path(sys.argv[1])
    else:
        cand = sorted((ROOT / "data").glob("*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not cand: sys.exit("no source export found — pass a path or put one in data/")
        src = cand[0]
    header, rows = read_export(src)
    template = rows[0]
    fixed = {header.index(b): b for b in BUILTINS if b in header}
    out_rows = []
    for n, (name, email) in enumerate(FAKE):
        row = [fake_cell(template[i], n, i) for i in range(len(header))]
        for i, b in fixed.items():
            row[i] = {"ID": n + 1, "Start time": 46000.5 + n, "Completion time": 46000.52 + n,
                      "Email": email, "Name": name, "Last modified time": None}[b]
        out_rows.append(row)
    write_xlsx(header, out_rows, OUT)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out_rows)} fake respondents x {len(header)} columns (header from {src.name})")

if __name__ == "__main__":
    main()
