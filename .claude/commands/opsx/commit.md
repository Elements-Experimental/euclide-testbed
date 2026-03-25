---
name: "OPSX: Commit"
description: Commit the change directory, push to spec/ branch, and open a PR to feat/
category: Workflow
tags: [workflow, artifacts, experimental]
---

Commit the spec artifacts, push to `spec/<slug>`, and open a PR targeting `feat/<slug>`.

**Input**: Optionally specify a change slug after `/opsx:commit`. If omitted, detected from current branch.

**Steps**

1. **Determine the change slug**

   - If an argument was provided, use it directly.
   - Otherwise, run `git branch --show-current` and strip the `spec/` prefix to get the slug.
   - If the current branch is not a `spec/*` branch, run `openspec list` and use the **AskUserQuestion tool** to let the user select the change.

2. **Verify branch**

   Confirm that the current branch is `spec/<slug>`. If not:
   - Warn: "You are not on `spec/<slug>`. Switch before committing."
   - Offer to switch: `git checkout spec/<slug>` (ask for confirmation first).
   - After switching, verify the current branch is now `spec/<slug>` before continuing.

3. **Stage and commit**

   ```bash
   git add openspec/changes/<slug>/
   git commit -m "spec(<slug>): add change artifacts"
   ```

4. **Push**

   ```bash
   git push -u origin spec/<slug>
   ```

5. **Read proposal body**

   Read `openspec/changes/<slug>/proposal.md`. If the file does not exist, use the fallback:
   > "No proposal.md found for change `<slug>`."

6. **Open PR to feat/ branch**

   ```bash
   gh pr create \
     --head spec/<slug> \
     --base feat/<slug> \
     --title "spec: <slug>" \
     --body "$(cat openspec/changes/<slug>/proposal.md)"
   ```

   (Use the fallback body if `proposal.md` is missing.)

7. **Report outcome**

   Output:
   - PR URL
   - Next step: "When this PR is merged, a GitHub workflow will create the change issue and `feat/<slug>` PR automatically."

**Guardrails**
- Fail clearly if `gh` is not authenticated (`gh auth status`)
- Fail if `feat/<slug>` branch does not exist remotely — the user must run `/opsx:new` or `/opsx:propose` first
- Do not commit files outside `openspec/changes/<slug>/`
- Do not push if the commit step fails
