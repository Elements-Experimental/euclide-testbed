---
name: openspec-ship
description: Finalize a verified change — merge the agent's implem branch into feat/, archive the change directory, squash feat/ into a clean two-commit history (spec + feat), update the draft PR body, and undraft it for team review. Run after walk confirms the implementation is correct.
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

   Infer slug from current branch by stripping the `implem-` prefix. If not on an `implem-*` branch, prompt with AskUserQuestion.

   Announce: "Shipping change: `<slug>`"

2. **Check verification status**

   Ask: "Has walk been completed successfully? (yes / no / skip)"

   If no: warn strongly before proceeding.

3. **Find the product issue number**

   Read `openspec/changes/<slug>/.meta` and extract `product_issue=N`.

4. **Read task groups for commit body**

   Extract `## N. Group name` headings from `openspec/changes/<slug>/tasks.md`.

5. **Show plan and confirm**

   Show what will happen:
   - Merge PR `implem-<slug>` → `feat/<slug>`
   - Archive change directory
   - Squash feat/ history into `spec(#N)` + `feat(#N)` commits
   - Update feat PR body
   - Undraft feat PR

6. **Merge the implem PR**

   Find the open PR from `implem-<slug>` targeting `feat/<slug>`:
   ```bash
   gh pr list --head implem-<slug> --base feat/<slug> --state open --json number --jq '.[0].number'
   gh pr merge <number> --merge
   ```

   Switch to `feat/<slug>` and pull:
   ```bash
   git checkout feat/<slug>
   git pull origin feat/<slug>
   ```

7. **Archive the change**

   Follow the archive command (`.claude/commands/opsx/archive.md`) to move `openspec/changes/<slug>/` to `openspec/changes/archive/YYYY-MM-DD-<slug>/`. Commit and push on `feat/<slug>`. This commit will be folded into the feat squash.

8. **Squash feat/ history**

   Identify the divergence point: the commit immediately after the last `spec(...)` commit on the branch. Reset to that point and create a single commit:
   ```
   feat(#N): <slug>

   - Group 1 name
   - Group 2 name
   - N. Documentation and design
   ```
   where `N` is the product issue number.

   Push with `--force-with-lease`. Final history: spec commit(s) + 1 feat commit (which includes all implementation work and the archive move).

9. **Update the feat PR body**

   Find the open draft PR `feat/<slug>` → `dev`. Read the product issue number and the spec-agent issue number (find spec issue by searching the product issue's comment history for "Spec task created: #N"). Update the PR body:

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

10. **Undraft the feat/ PR**

    ```bash
    gh pr ready <number>
    ```

11. **Report outcome**: commit message, archive path, PR URL, next step.

**Guardrails**
- Use `--force-with-lease`, never `--force`
- Do not squash spec-phase commits — only squash from the first post-spec commit onwards
- Merge the implem PR with a regular merge (not squash); the squash happens once on feat/ after
- Do not merge the feat PR — team reviews first
- Confirm the plan before executing
