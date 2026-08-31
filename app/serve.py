"""PROTOTYPE - wayfinder ticket #26: local app architecture.

Question this answers: how is the v2 app built, fed, and launched?
  drop the raw Forms .xlsx in data/ -> `python app/serve.py` -> dashboard on localhost.

What is real here:            what is stubbed:
  - finding the export          - score(): v2 scoring rules are ticket #28.
  - parsing it (stdlib only)      Until then /scored.csv serves the v1 sample
  - label -> number               (scoring/scored-sample.csv) so the render
  - the http server + seam        path is visible end to end.
  - error cases

Seam: Python computes, the browser draws. The template (dashboard/index.html)
is served UNMODIFIED at "/" and fed via its existing ?csv= fetch path.
/parsed.json shows the real parsed export crossing the same wire.
Stdlib only, on purpose: any Python 3, no venv, no pip install.
"""
import io, json, re, sys, webbrowser, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PORT = 8737
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
BUILTINS = {"ID", "Start time", "Completion time", "Email", "Name", "Last modified time"}

def fail(msg):
    print(f"\n  problem: {msg}\n", file=sys.stderr)
    sys.exit(1)

# ---- 1. find the export -----------------------------------------------------
def find_export(argv):
    argv = [a for a in argv if a != "--no-browser"]
    if len(argv) > 1:
        p = Path(argv[1])
        if not p.is_file(): fail(f"no file at {p}")
        return p
    DATA.mkdir(exist_ok=True)
    files = sorted(DATA.glob("*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        fallback = sorted((ROOT / "Excel Example").glob("*.xlsx"))
        if fallback:
            print(f"  data/ is empty - falling back to the v1 fixture in 'Excel Example/'.")
            return fallback[0]
        fail(f"no .xlsx found. Drop the raw Forms export into {DATA} and run again.")
    if len(files) > 1:
        print(f"  {len(files)} .xlsx files in data/ - using the newest, ignoring: "
              + ", ".join(p.name for p in files[1:]))
    return files[0]

# ---- 2. parse it (stdlib zip + XML; the export is a zip of XML) -------------
def cell_ref_to_col(ref):
    n = 0
    for ch in ref:
        if ch.isdigit(): break
        n = n * 26 + ord(ch) - 64
    return n - 1

def parse_export(path):
    try:
        z = zipfile.ZipFile(path)
        shared = [ "".join(t.text or "" for t in si.findall(".//m:t", NS))
                   for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS) ]
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
    blank = [i for i, h in enumerate(header) if not h]
    dupes = sorted({h for h in header if h and header.count(h) > 1})
    # columns resolve by HEADER TEXT (the statement), never by position
    rows = [ { header[i]: r.get(i) for i in range(width) if header[i] } for r in grid[1:] ]
    return header, rows, blank, dupes

# label -> number: Forms exports label text; ours lead with the digit ("5 - Always")
def label_num(label):
    if label is None: return None
    m = re.match(r"\s*(\d+)\b", label)
    return int(m.group(1)) if m else None   # None: N/A, checklists, free text

# ---- 3. score (STUB - ticket #28 owns the real rules) -----------------------
def score(header, rows):
    sample = ROOT / "scoring" / "scored-sample.csv"
    return sample.read_text(encoding="utf-8") if sample.is_file() else "schema\n"

# ---- 4. serve ---------------------------------------------------------------
def main():
    src = find_export(sys.argv)
    header, rows, blank, dupes = parse_export(src)
    stmts = [h for h in header if h and h not in BUILTINS]
    answered = sum(1 for r in rows for h in stmts if r.get(h) is not None)
    numeric = sum(1 for r in rows for h in stmts if label_num(r.get(h)) is not None)
    names = ", ".join((r.get("Name") or "?") for r in rows)

    print(f"\n  export : {src.name}")
    print(f"  parsed : {len(rows)} respondent(s) ({names}), {len(header)} columns "
          f"({len(stmts)} statements + {len(header)-len(stmts)-len(blank)} built-ins)")
    print(f"  answers: {answered} filled, {numeric} resolve to a number by their leading digit")
    if blank: print(f"  warning: {len(blank)} blank header column(s) at {blank} - ignored")
    if dupes: print(f"  warning: duplicate statement headers (item text is the key!): {dupes}")

    scored_csv = score(header, rows)
    template = (ROOT / "dashboard" / "index.html").read_bytes()
    parsed_json = json.dumps(
        {"file": src.name, "respondents": rows,
         "numeric": [{h: label_num(r.get(h)) for h in stmts} for r in rows]},
        ensure_ascii=False).encode("utf-8")

    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            routes = {
                "/scored.csv":  ("text/csv; charset=utf-8", scored_csv.encode("utf-8")),
                "/parsed.json": ("application/json; charset=utf-8", parsed_json),
            }
            if self.path == "/":                       # feed the template its CSV via its own ?csv= path
                self.send_response(302); self.send_header("Location", "/?csv=/scored.csv"); self.end_headers()
            elif self.path.startswith("/?"):
                self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers(); self.wfile.write(template)
            elif self.path in routes:
                ctype, body = routes[self.path]
                self.send_response(200); self.send_header("Content-Type", ctype)
                self.end_headers(); self.wfile.write(body)
            else:
                self.send_error(404)
        def log_message(self, *a): pass

    url = f"http://localhost:{PORT}/"
    print(f"\n  dashboard: {url}   (scored data is the v1 SAMPLE until #28 lands;")
    print(f"  your real parsed export is at {url}parsed.json)  Ctrl+C stops it.\n")
    if "--no-browser" not in sys.argv: webbrowser.open(url)
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
    except KeyboardInterrupt:
        print("  stopped.")

if __name__ == "__main__":
    main()
