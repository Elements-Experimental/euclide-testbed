---
name: "OPSX: New"
description: Start a new change using the experimental artifact workflow (OPSX)
category: Workflow
tags: [workflow, artifacts, experimental]
---

Start a new change using the experimental artifact-driven approach.

**Input**: The argument after `/opsx:new` is the change name (kebab-case), OR a description of what the user wants to build.

**Steps**

1. **If no input provided, ask what they want to build**

   Use the **AskUserQuestion tool** (open-ended, no preset options) to ask:
   > "What change do you want to work on? Describe what you want to build or fix."

   From their description, derive a kebab-case name (e.g., "add user authentication" → `add-user-auth`).

   **IMPORTANT**: Do NOT proceed without understanding what the user wants to build.

2. **Determine the workflow schema**

   Use the default schema (omit `--schema`) unless the user explicitly requests a different workflow.

   **Use a different schema only if the user mentions:**
   - A specific schema name → use `--schema <name>`
   - "show workflows" or "what workflows" → run `openspec schemas --json` and let them choose

   **Otherwise**: Omit `--schema` to use the default.

3. **Determine the base branch (Step A)**

   Run `git ls-remote --heads origin dev` to check whether `dev` exists.
   - If it exists, default base is `dev`
   - If not, default base is `main`

   Also run `git branch -r` to get all remote branches.

   Use the **AskUserQuestion tool** to ask:
   > "Which branch should `feat/<slug>` be based on?"

   Show the available remote branches as options, with the detected default pre-selected.

4. **Check for existing branches (Step B)**

   Run:
   ```bash
   git ls-remote --heads origin feat/<slug> spec/<slug>
   ```

   If either branch already exists, use the **AskUserQuestion tool** to ask:
   > "Branch(es) feat/<slug> and/or spec/<slug> already exist. Reuse them or abort?"

   Options: "Reuse existing branches", "Abort"

   - If **reuse**: run `git fetch origin && git checkout spec/<slug>` and skip Step C. Continue from step 5.
   - If **abort**: stop and tell the user to use `/opsx:continue` to resume an existing change.

5. **Create branches (Step C)**

   _(Skip if reusing existing branches from Step B.)_

   ```bash
   git fetch origin
   git checkout -b feat/<slug> origin/<base>
   git push -u origin feat/<slug>
   git checkout -b spec/<slug> feat/<slug>
   git push -u origin spec/<slug>
   ```

6. **Create the change directory**
   ```bash
   openspec new change "<name>"
   ```
   Add `--schema <name>` only if the user requested a specific workflow.
   This creates a scaffolded change at `openspec/changes/<name>/` with the selected schema.

7. **Show the artifact status**
   ```bash
   openspec status --change "<name>"
   ```
   This shows which artifacts need to be created and which are ready (dependencies satisfied).

8. **Get instructions for the first artifact**
   The first artifact depends on the schema. Check the status output to find the first artifact with status "ready".
   ```bash
   openspec instructions <first-artifact-id> --change "<name>"
   ```
   This outputs the template and context for creating the first artifact.

9. **STOP and wait for user direction**

**Output**

After completing the steps, summarize:
- Change name and location
- Branches created (or reused): `feat/<slug>` and `spec/<slug>` (based on `<base>`)
- You are now on `spec/<slug>` — ready to start writing the spec
- Schema/workflow being used and its artifact sequence
- Current status (0/N artifacts complete)
- The template for the first artifact
- Prompt: "Ready to create the first artifact? Run `/opsx:continue` or just describe what this change is about and I'll draft it."

**Guardrails**
- Do NOT create any artifacts yet - just show the instructions
- Do NOT advance beyond showing the first artifact template
- If the name is invalid (not kebab-case), ask for a valid name
- If a change with that name already exists, suggest using `/opsx:continue` instead
- Pass --schema if using a non-default workflow
- Fail clearly if `git` or `gh` commands fail; do not proceed with partial state
