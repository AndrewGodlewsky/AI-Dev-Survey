# Wayfinder — local markdown tracker

No issue tracker is configured for this repo, so the wayfinder map lives here.

- `MAP.md` — the map (label `wayfinder:map`).
- `tickets/NNN-slug.md` — child tickets. Frontmatter: `type` (research | prototype | grilling | task), `status` (open | closed), `assignee` (empty = unclaimed), `blocked_by` (ticket numbers).
- **Claim** a ticket by setting `assignee` before starting work.
- **Frontier** = `status: open`, `assignee` empty, every `blocked_by` ticket `status: closed`.
  Query: `grep -l "status: open" tickets/*.md` then check `assignee` / `blocked_by`.
- **Resolve** by appending `## Resolution` to the ticket, setting `status: closed`, and adding a one-line pointer under *Decisions so far* in `MAP.md`.
- **Work a ticket**: `/wayfinder wayfinder/MAP.md` (optionally naming a ticket).
