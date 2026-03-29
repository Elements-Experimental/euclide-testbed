---
name: openspec-walk
description: Walk the developer step-by-step through the test protocol for a change. At each human checkpoint, pause for validation. Handle issues inline. After all steps pass, run verification.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: euclide
  version: "1.0"
---

Walk the developer through the test protocol for a change, handling issues inline and running verification at the end.

**Input**: Optionally specify a change slug. If omitted, infer from current branch or prompt.

**Steps**

1. **Select the change**

   If a slug is provided, use it. Otherwise infer from current branch (strip the branch type prefix — everything up to and including the first `/`). If ambiguous, use AskUserQuestion.

   Announce: "Walking protocol for change: `<slug>`"

2. **Load the protocol**

   Read `openspec/changes/<slug>/protocol.md`.

   If missing: warn, offer to draft from spec scenarios, ask developer to review before proceeding.

3. **Run setup steps**

   Present each `## Setup` item; confirm done before continuing.

4. **Run automated baseline (before human walkthrough)**

   Before asking the developer to verify anything manually, run the automated checks. Read `docs/testing.md` to find the test and lint commands for this project.

   Announce upfront what you're about to run:
   > "Running automated baseline before walkthrough: [list commands]"

   Run each command and collect results. Then report clearly:
   - ✓ Tests: `N passed` (or "no test suite configured")
   - ✓ Lint: clean (or issues found)
   - ✓ Type check: clean (or errors found)

   **If a command is not found or no test file exists**: note it as "not configured" and continue — do not block. Absence of a test suite is not a failure.

   **If tests fail or lint errors exist**: surface them now with the full output. Ask the developer: "Fix before walkthrough, or note in PR and continue?" Do not force a fix — the developer decides.

   This baseline gives both you and the developer a clean starting point before any manual step is attempted.

5. **Walk through protocol steps**

   For each `### Step N.M` with `<!-- HUMAN CHECKPOINT -->`:
   - Display: step name, action, expected result
   - Pause: "Passed / Failed / Skip?"
   - If **passed**: continue
   - If **failed**: enter issue resolution mode
   - If **skipped**: note and continue

6. **Issue resolution mode**

   When a step fails:
   - Ask developer to describe what happened
   - Diagnose: implementation issue vs. spec issue
   - **Implementation issue**: fix code, run tests, commit `fix(#N): <desc>`, update tasks.md checkboxes
   - **Spec issue**: require developer confirmation, then edit spec file, commit `spec(<slug>): adjust <req>`
   - Offer to re-check earlier steps affected by the fix
   - Continue from the failed step

7. **Run verification after all steps pass**

   Run `openspec instructions apply --change "<slug>" --json` to get context files, then perform completeness / correctness / coherence checks (see openspec-verify-change skill).

8. **Handle verification issues**

   For CRITICAL issues: enter issue resolution mode per issue, re-run verify after each fix.

   For WARNINGs: present and ask "Fix now or note for PR?"

9. **Report outcome**: step-by-step pass/fail log, final verify report, next step (run ship skill).

**Guardrails**
- Never skip a HUMAN CHECKPOINT step without developer confirmation
- Never modify spec files without developer confirmation
- After any code fix, offer to re-check affected earlier steps
- Do not invoke ship — that is the developer's explicit action
