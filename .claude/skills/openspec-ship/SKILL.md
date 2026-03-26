---
name: openspec-ship
description: Finalize a verified change — merge the agent's implem branch into the integration branch, archive the change directory, squash the integration branch into a clean two-commit history (spec + type), update the draft PR body, and undraft it for team review. Run after walk confirms the implementation is correct.
license: MIT
compatibility: Requires gh CLI authenticated.
metadata:
  author: euclide
  version: "2.0"
---

Finalize a verified change: merge the implem branch, archive, squash, update the PR, undraft.

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
   - Archive change directory on `<integration-branch>`
   - Squash `<integration-branch>` history into `spec(#N)` + `<type>(#N)` commits
   - Update draft PR body
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

   Follow the archive command (`.claude/commands/opsx/archive.md`) to move `openspec/changes/<slug>/` to `openspec/changes/archive/YYYY-MM-DD-<slug>/`. Commit and push on `<integration-branch>`. This commit will be folded into the squash below.

9. **Squash the integration branch**

   Identify the divergence point: the commit immediately after the last `spec(...)` commit on the branch. Reset to that point and create a single commit:
   ```
   <type>(#N): <slug>

   - Group 1 name
   - Group 2 name
   - N. Documentation and design
   ```
   where `<type>` is `branch_type` from `.meta` and `N` is the product issue number.

   Push with `--force-with-lease`. Final history: spec commit(s) + 1 `<type>` commit (which includes all implementation work and the archive move).

10. **Update the draft PR body**

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

11. **Undraft the PR**

    ```bash
    gh pr ready <number>
    ```

12. **Report outcome**: commit message, archive path, PR URL, next step.

**Guardrails**
- Use `--force-with-lease`, never `--force`
- Do not squash spec-phase commits — only squash from the first post-spec commit onwards
- Merge the implem PR with a regular merge (not squash); the squash happens once on the integration branch after
- Archive before squashing so the archive commit is included in the type commit
- Do not merge the feat PR — team reviews first
- Confirm the plan before executing
