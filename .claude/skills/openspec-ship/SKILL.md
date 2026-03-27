---
name: openspec-ship
description: Finalize a verified change — merge the agent's implem branch into the integration branch, archive the change directory (including syncing delta specs to main specs), squash the integration branch into a single clean commit, update the draft PR body, and undraft it for team review. Run after walk confirms the implementation is correct.
license: MIT
compatibility: Requires gh CLI authenticated.
metadata:
  author: euclide
  version: "2.1"
---

Finalize a verified change: merge the implem branch, archive, update the PR, squash, undraft.

**Input**: Optionally specify a change slug. If omitted, infer from current branch.

**Steps**

1. **Select the change**

   Infer slug from current branch by stripping everything up to and including the first `-` after `implem` (i.e., strip `implem-` prefix). If not on an `implem-*` branch, prompt with AskUserQuestion.

   Announce: "Shipping change: `<slug>`"

2. **Check verification status**

   Ask: "Has walk been completed successfully? (yes / no / skip)"

   If no: warn strongly before proceeding.

3. **Read .meta**

   Read `openspec/changes/<slug>/.meta` and extract:
   - `product_issue=N` — the product issue number
   - `branch_type=feat` (or fix/chore/docs) — the commit type
   - `branch=feat/<slug>` — the integration branch name

   Fall back to `feat/<slug>` if `branch` is absent (older repos).

4. **Read task groups for commit body**

   Extract `## N. Group name` headings from `openspec/changes/<slug>/tasks.md`.

5. **Find the implem issue**

   Search for the open implementation issue:
   ```bash
   gh issue list --state open --label spec-driven \
     --search "implem: ${SLUG} in:title" \
     --json number --jq '.[0].number'
   ```

6. **Show plan and confirm**

   Show what will happen:
   - Merge PR `implem-<slug>` (or `<agent>/implem-<slug>`) → `<integration-branch>` and close implem issue
   - Sync delta specs to main specs (if any exist), then archive change directory on `<integration-branch>`
   - Update draft PR body
   - Squash `<integration-branch>` into a single `<type>(#N)` commit
   - Undraft PR

7. **Merge the implem PR and close the implem issue**

   Find the open PR targeting the integration branch with title starting `implem: <slug>`:
   ```bash
   gh pr list --base <integration-branch> --state open \
     --search "implem: ${SLUG}" \
     --json number --jq '.[0].number'
   ```

   Merge it (regular merge — squash will happen on the integration branch afterwards):
   ```bash
   gh pr merge <number> --merge
   ```

   Close the implem issue:
   ```bash
   gh issue close <impl-issue> --reason completed
   ```

   Switch to the integration branch and pull:
   ```bash
   git checkout <integration-branch>
   git pull origin <integration-branch>
   ```

8. **Archive the change**

   Run the full archive process (openspec-archive-change skill) for `<slug>`:
   - Check `openspec/changes/<slug>/specs/` for delta specs. If any exist, show the sync
     summary and prompt to sync them to main specs before archiving (recommended).
   - Move `openspec/changes/<slug>/` → `openspec/changes/archive/YYYY-MM-DD-<slug>/`.

   Commit and push the archive (and any spec sync) on `<integration-branch>`.
   This commit will be folded into the squash below.

9. **Update the draft PR body**

    Find the open draft PR `<integration-branch>` → `dev`. Read the spec-agent issue number from the product issue's comment history (look for "Spec task created: #N"). Update the PR body:

    ```
    {contents of openspec/changes/archive/YYYY-MM-DD-<slug>/proposal.md}

    ---

    ## Implementation

    - Group 1 name
    - Group 2 name

    closes #<impl-issue>
    closes #<product-issue>
    closes #<spec-issue>
    ```

    Use `gh pr edit <number> --body-file <tempfile>` to apply.

10. **Squash the integration branch**

    Reset the integration branch to its upstream base (the commit the branch diverged from) and create a single commit:
    ```
    <type>(#N): <slug>

    - Group 1 name
    - Group 2 name
    - N. Documentation and design
    ```
    where `<type>` is `branch_type` from `.meta` and `N` is the product issue number.

    Push with `--force-with-lease`.

11. **Undraft the PR**

    ```bash
    gh pr ready <number>
    ```

12. **Verify final state**

    a. **Archive integrity** — confirm:
       - `openspec/changes/<slug>/` no longer exists
       - `openspec/changes/archive/YYYY-MM-DD-<slug>/` exists and contains at minimum `proposal.md`, `tasks.md`, `.meta`
       If missing or malformed, abort with a clear error.

    b. **Spec sync** — if `openspec/changes/archive/YYYY-MM-DD-<slug>/specs/` is non-empty, confirm that each capability directory listed there has a corresponding `openspec/specs/<capability>/spec.md`. If any main spec file is absent, abort with: "Delta specs were not merged — run /opsx:sync before shipping."

    c. **Branch shape** — run `git log --oneline <integration-branch>` and confirm the history is exactly **one commit** with message `<type>(#N): <slug>`. If there is more than one commit, or HEAD does not match, abort with a clear error describing the actual state.

    Only if all three checks pass: proceed to the outcome report.

13. **Report outcome**: commit message, archive path, PR URL, next step.

**Guardrails**
- Use `--force-with-lease`, never `--force`
- Merge the implem PR with a regular merge (not squash); the squash happens once on the integration branch after
- Archive before squashing so the archive commit is included in the squash
- Update the PR body before squashing — the squash force-push is the last mutation before undrafting
- Squash the entire integration branch into a single `<type>(#N)` commit
- Verify archive integrity, spec sync, and branch shape before reporting success — a failed squash or incomplete move must surface as an error, not a silent partial ship
- Do not merge the feat PR — team reviews first
- Confirm the plan before executing
