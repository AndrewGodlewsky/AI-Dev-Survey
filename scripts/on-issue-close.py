"""PostToolUse hook: after `gh issue close N`, refresh the README progress block,
then commit everything in the working tree and push to main.

Commit message = the closed issue's title + its body (the Question).
Dry run by hand:  echo '{"tool_input":{"command":"gh issue close 3"}}' | python scripts/on-issue-close.py --dry-run
"""
import json, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv


def run(*args, check=True):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=check).stdout.strip()


def out(**fields):
    print(json.dumps(fields))
    sys.exit(0)


def main():
    try:
        cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    except Exception:
        return
    m = re.search(r"gh issue close\s+(?:\S+/issues/)?(\d+)", cmd)
    if not m:
        return
    n = m.group(1)

    # 1. README block (idempotent; errors here should not stop the commit)
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "update-readme.py"), "--force"],
                   cwd=ROOT, capture_output=True)

    # 2. Guards
    branch = run("git", "rev-parse", "--abbrev-ref", "HEAD")
    if branch != "main":
        out(systemMessage=f"on-issue-close: on branch '{branch}', not main — nothing committed or pushed.")
    run("git", "add", "-A")
    if not run("git", "status", "--porcelain"):
        out(systemMessage=f"on-issue-close: issue #{n} closed but the working tree is clean — nothing to commit.")

    # 3. Message from the issue
    issue = json.loads(run("gh", "issue", "view", n, "--json", "title,body,url"))
    body = re.sub(r"^## Question\s*", "", issue["body"].strip()).strip()
    msg = (f"Resolve #{n}: {issue['title']}\n\n{body}\n\n{issue['url']}\n\n"
           "Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>")

    if DRY:
        print("--- would commit on", branch, "---\n" + msg + "\n--- staged:\n" + run("git", "status", "--porcelain"))
        run("git", "reset", "-q")  # unstage; dry run leaves the tree as it was
        return

    # 4. Commit + push
    try:
        subprocess.run(["git", "commit", "-q", "-F", "-"], cwd=ROOT, input=msg, text=True,
                       encoding="utf-8", capture_output=True, check=True)
        run("git", "push", "-q", "origin", "main")
    except subprocess.CalledProcessError as e:
        out(systemMessage=f"on-issue-close: git failed — {e.stderr.strip() or e}. Commit/push may be incomplete; check `git status`.")
    out(systemMessage=f"on-issue-close: committed and pushed to main — Resolve #{n}: {issue['title']}",
        hookSpecificOutput={"hookEventName": "PostToolUse", "additionalContext":
            "README.md progress block was regenerated and the working tree was committed and pushed to main. "
            "If this ticket's resolution changed how the project works, update the README prose in a follow-up."})


if __name__ == "__main__":
    main()
