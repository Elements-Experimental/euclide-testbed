---
name: openspec-ship
description: Finalize a verified change — squash implementation commits into one, archive the change directory, undraft the feat/ PR, and surface it for team review. Run after walk confirms the implementation is correct.
license: MIT
compatibility: Requires openspec CLI and gh CLI authenticated.
metadata:
  author: euclide
  version: "1.0"
---

Finalize a verified change: squash commits, archive the change, undraft the PR.

**Input**: Optionally specify a change slug. If omitted, infer from current branch or prompt.

**Steps**

1. **Select the change**

   If a slug is provided, use it. Otherwise infer from current branch (strip `feat/`). If ambiguous, use AskUserQuestion.

   Announce: "Shipping change: `<slug>`"

2. **Verify current branch**

   Confirm on `feat/<slug>`. Check working tree is clean.

3. **Check verification status**

   Ask: "Has walk been completed successfully? (yes / no / skip)"

   If no: warn strongly before proceeding.

4. **Find the issue number**

   Read tasks.md or git log to find `#N` from commit messages. Ask if ambiguous.

5. **Read task groups for commit body**

   Extract `## N. Group name` headings from `openspec/changes/<slug>/tasks.md`.

6. **Show squash plan and confirm**

   List the implementation commits to be squashed. Ask developer to confirm.

7. **Squash implementation commits**

   Reset to the divergence point (first commit after spec phase) and create a single commit:
   ```
   feat(#N): <slug>

   - Group 1 name
   - Group 2 name
   - N. Documentation and design
   ```

   Push with `--force-with-lease`.

8. **Archive the change**

   Follow the archive command (`.claude/commands/opsx/archive.md`) to move `openspec/changes/<slug>/` to `openspec/changes/archive/YYYY-MM-DD-<slug>/`. Commit and push.

9. **Undraft the feat/ PR**

   ```bash
   gh pr list --head feat/<slug> --state open --json number
   gh pr ready <number>
   ```

10. **Report outcome**: commit message, archive path, PR URL, next step.

**Guardrails**
- Use `--force-with-lease`, never `--force`
- Do not squash spec-phase commits
- Do not merge the PR — team reviews first
- Confirm squash plan before executing
