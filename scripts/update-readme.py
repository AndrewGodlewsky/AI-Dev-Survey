"""Regenerate the auto-maintained block in README.md from GitHub + the working tree.

Runs as a Claude Code PostToolUse hook (stdin = hook JSON) after `gh issue close`,
or by hand:  python scripts/update-readme.py --force
"""
import json, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
REPO_URL = "https://github.com/AndrewGodlewsky/AI-Dev-Survey"
START, END = "<!-- progress:start -->", "<!-- progress:end -->"

# Deliverables the map is building; ticked when the file exists on disk.
ARTIFACTS = [
    ("Survey document", "survey/SURVEY.md"),
    ("Coverage grid", "survey/coverage-grid.md"),
    ("Rubric", "rubric/RUBRIC.md"),
    ("Scoring sheet (Excel)", "scoring/scoring.xlsx"),
    ("Dashboard (HTML)", "dashboard/index.html"),
    ("How to read the results", "docs/HOW-TO-READ.md"),
]


def hook_should_run():
    if "--force" in sys.argv:
        return True
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return False
    return "issue close" in payload.get("tool_input", {}).get("command", "")


def gh_issues():
    out = subprocess.run(
        ["gh", "issue", "list", "--state", "all", "--limit", "200",
         "--json", "number,title,state,labels"],
        capture_output=True, text=True, encoding="utf-8", check=True).stdout
    issues = []
    for i in json.loads(out):
        labels = [l["name"] for l in i["labels"]]
        types = [l.split(":", 1)[1] for l in labels if l.startswith("wayfinder:")]
        if not types or "map" in types:
            continue
        issues.append(dict(n=i["number"], title=i["title"], closed=i["state"] == "CLOSED", type=types[0]))
    return sorted(issues, key=lambda i: i["n"])


def render(issues):
    link = lambda i: f"[{i['title']}]({REPO_URL}/issues/{i['n']})"
    done = [i for i in issues if i["closed"]]
    todo = [i for i in issues if not i["closed"]]
    lines = [START, "",
             f"**Map progress:** {len(done)} of {len(issues)} tickets resolved.", "",
             "### Deliverables", ""]
    for name, path in ARTIFACTS:
        box = "x" if os.path.exists(os.path.join(ROOT, path)) else " "
        lines.append(f"- [{box}] {name} — `{path}`")
    lines += ["", "### Decided", ""]
    lines += [f"- {link(i)}" for i in done] or ["- _nothing yet_"]
    lines += ["", "### Still open", ""]
    lines += [f"- {link(i)} _({i['type']})_" for i in todo] or ["- _none — the map is complete_"]
    lines += ["", END]
    return "\n".join(lines)


def main():
    if not hook_should_run():
        return
    text = open(README, encoding="utf-8").read()
    if START not in text or END not in text:
        print(json.dumps({"systemMessage": "README.md has no progress block; skipped."}))
        return
    new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: render(gh_issues()), text, flags=re.S)
    changed = new != text
    if changed:
        open(README, "w", encoding="utf-8", newline="\n").write(new)
    if "--force" in sys.argv:
        print("README progress block " + ("updated." if changed else "already current."))
        return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": (
            "README.md progress block was regenerated from GitHub. A ticket was just closed: "
            "if its resolution changed what the project is or how the survey/rubric/scoring/dashboard "
            "works, update the prose sections of README.md (above the progress block) to match. "
            "Leave the block between the progress markers alone — it is generated.")}}))


if __name__ == "__main__":
    main()
