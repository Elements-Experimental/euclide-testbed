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

   If a slug is provided, use it. Otherwise infer from current branch (strip `feat/`). If ambiguous, use AskUserQuestion.

   Announce: "Walking protocol for change: `<slug>`"

2. **Load the protocol**

   Read `openspec/changes/<slug>/protocol.md`.

   If missing: warn, offer to draft from spec scenarios, ask developer to review before proceeding.

3. **Run setup steps**

   Present each `## Setup` item; confirm done before continuing.

4. **Walk through protocol steps**

   For each `### Step N.M` with `<!-- HUMAN CHECKPOINT -->`:
   - Display: step name, action, expected result
   - Pause: "Passed / Failed / Skip?"
   - If **passed**: continue
   - If **failed**: enter issue resolution mode
   - If **skipped**: note and continue

5. **Issue resolution mode**

   When a step fails:
   - Ask developer to describe what happened
   - Diagnose: implementation issue vs. spec issue
   - **Implementation issue**: fix code, run tests, commit `fix(#N): <desc>`, update tasks.md checkboxes
   - **Spec issue**: require developer confirmation, then edit spec file, commit `spec(<slug>): adjust <req>`
   - Offer to re-check earlier steps affected by the fix
   - Continue from the failed step

6. **Run verification after all steps pass**

   Run `openspec instructions apply --change "<slug>" --json` to get context files, then perform completeness / correctness / coherence checks (see openspec-verify-change skill).

7. **Handle verification issues**

   For CRITICAL issues: enter issue resolution mode per issue, re-run verify after each fix.

   For WARNINGs: present and ask "Fix now or note for PR?"

8. **Report outcome**: step-by-step pass/fail log, final verify report, next step (run ship skill).

**Guardrails**
- Never skip a HUMAN CHECKPOINT step without developer confirmation
- Never modify spec files without developer confirmation
- After any code fix, offer to re-check affected earlier steps
- Do not invoke ship — that is the developer's explicit action
