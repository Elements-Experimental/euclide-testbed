---
name: "OPSX: Ship"
description: Squash implementation commits, archive the change, undraft the feat/ PR, and prepare it for final review
category: Workflow
tags: [workflow, ship, archive]
---

Finalize a verified change: squash implementation commits into one, archive the change directory, undraft the PR, and surface it for team review.

Run this after `/opsx:walk` confirms the implementation is correct.

**Input**: Optionally specify a change slug (e.g., `/opsx:ship 42-add-auth`). If omitted, infer from current branch or prompt.

**Steps**

1. **Select the change**

   If a slug is provided, use it. Otherwise:
   - Infer from current branch: strip `feat/` prefix
   - If ambiguous, run `openspec list --json` and use **AskUserQuestion** to select

   Always announce: "Shipping change: `<slug>`"

2. **Verify current branch and state**

   Confirm the current branch is `feat/<slug>`. If not:
   ```bash
   git checkout feat/<slug>
   ```

   Check that working tree is clean:
   ```bash
   git status --short
   ```
   If there are uncommitted changes, warn and ask: "You have uncommitted changes. Stash or commit them first?"

3. **Check verification status**

   Ask: "Has `/opsx:walk` been completed successfully for this change? (yes / no / skip)"

   If no: warn strongly — "Shipping without verification may introduce unverified changes. Proceed anyway?"

   If skip: proceed without warning (developer knows what they're doing).

4. **Find the issue number**

   Read `openspec/changes/<slug>/tasks.md` to find the issue number, or check git log:
   ```bash
   git log --oneline feat/<slug> | head -20
   ```
   Parse issue number `#N` from commit messages. If ambiguous, use **AskUserQuestion**.

5. **Read task groups for commit body**

   Read `openspec/changes/<slug>/tasks.md`. Extract the `## N. Group name` headings to build the commit body:
   ```
   feat(#N): <slug>

   - Group 1 name
   - Group 2 name
   - Group 3 name
   ```

6. **Squash implementation commits**

   Find the base commit (the last commit on `feat/<slug>` that was NOT part of the implementation — typically the `.meta` init commit or the last commit from the spec phase):
   ```bash
   git log --oneline feat/<slug>
   ```

   Identify the divergence point (first commit after `spec/<slug>` was merged). All commits after that point are implementation commits.

   Squash them:
   ```bash
   git reset --soft <base-commit>
   git commit -m "feat(#N): <slug>

   - Group 1 name
   - Group 2 name
   - N. Documentation and design"
   ```

   Push:
   ```bash
   git push --force-with-lease origin feat/<slug>
   ```

7. **Archive the change**

   Run the archive skill:
   ```bash
   # Equivalent of /opsx:archive <slug>
   ```
   Follow `.claude/commands/opsx/archive.md` to move `openspec/changes/<slug>/` to `openspec/changes/archive/YYYY-MM-DD-<slug>/`.

   Commit and push the archive:
   ```bash
   git add openspec/changes/
   git commit -m "chore(<slug>): archive change"
   git push origin feat/<slug>
   ```

8. **Undraft the feat/ PR**

   Find the feat/ PR:
   ```bash
   gh pr list --head feat/<slug> --state open --json number,url
   ```

   Undraft it:
   ```bash
   gh pr ready <PR-number>
   ```

9. **Report outcome**

   Output:
   ```
   ## Shipped: <slug>

   ✓ Commits squashed into: feat(#N): <slug>
   ✓ Change archived to: openspec/changes/archive/YYYY-MM-DD-<slug>/
   ✓ PR ready for review: <PR-URL>

   Next: Request a review from your team on the PR above.
   ```

**Guardrails**
- Use `--force-with-lease` (not `--force`) when pushing the squashed commit
- Do not squash commits that belong to the spec phase (`.meta` init, spec artifact commits)
- Do not close or merge the PR — that is for the team after review
- If the archive step fails, abort and report — do not push the squashed commit without archiving
- Confirm the squash plan with the developer before executing: show the list of commits to be squashed
