---
name: "OPSX: Walk"
description: Walk the developer step-by-step through the test protocol, handle issues inline, then run verification
category: Workflow
tags: [workflow, verify, protocol]
---

Walk the developer through the test protocol for a change, one step at a time. At each human checkpoint, pause and wait for validation. Handle any issues discovered before continuing. After all steps pass, run verification against the spec.

**Input**: Optionally specify a change slug (e.g., `/opsx:walk 42-add-auth`). If omitted, infer from current branch or prompt.

**Steps**

1. **Select the change**

   If a slug is provided, use it. Otherwise:
   - Infer from current branch: strip `feat/` prefix
   - If ambiguous, run `openspec list --json` and use **AskUserQuestion** to select

   Always announce: "Walking protocol for change: `<slug>`"

2. **Load the protocol**

   Read `openspec/changes/<slug>/protocol.md`.

   If the file does not exist:
   - Warn: "No protocol.md found for `<slug>`. The implementation agent should have written this."
   - Offer to generate one from the specs: "Would you like me to draft a protocol.md from the spec scenarios? (It will need your review)"
   - If yes: read `openspec/changes/<slug>/specs/*/spec.md` and draft `protocol.md` using the schema template; ask the developer to review before proceeding

   Parse protocol into sections (by `## N.` headings) and steps (by `### Step N.N` headings).

3. **Run setup steps**

   Present the `## Setup` section. For each `- [ ]` item, show it to the developer and ask them to confirm it is done before continuing:
   ```
   Setup: <item>
   Done? (yes / skip)
   ```

4. **Walk through protocol steps**

   For each step in order:

   a. Display the step:
   ```
   ─────────────────────────────────────────
   Step N.M — <Step name>
   Action: <action from - [ ] line>
   Expected: <expected result>
   ─────────────────────────────────────────
   ```

   b. If the step has `<!-- HUMAN CHECKPOINT -->`, pause and ask:
   ```
   → Perform the action above, then report back:
     1. Passed — everything looks correct
     2. Failed — something is wrong
     3. Skip — not applicable
   ```

   c. **If passed**: mark the step mentally as passed, continue to next step.

   d. **If failed**: enter issue resolution mode (see below).

   e. **If skipped**: note it in the session log, continue.

5. **Issue resolution mode**

   When a step fails:

   a. Ask the developer to describe what they observed.

   b. Diagnose: is this an **implementation issue** or a **spec issue**?
      - **Implementation issue** (the code doesn't match the spec): help fix the code
        - Make necessary code changes
        - Run automated tests: `docs/testing.md`
        - Commit: `fix(#N): <description>`
        - Update `openspec/changes/<slug>/tasks.md` checkboxes if tasks were modified
      - **Spec issue** (the spec doesn't reflect what was agreed): **require developer confirmation before any spec change**
        - Explain: "This would require changing the spec. Spec changes must be intentional — they affect what 'done' means."
        - Ask: "Do you want to update the spec to reflect this? (yes / no)"
        - If yes: edit the relevant `openspec/changes/<slug>/specs/<capability>/spec.md` and commit: `spec(<slug>): adjust <requirement> per verification`

   c. After fixing, re-check previously passed steps that could be affected:
      - Ask: "Should I re-check earlier steps that may be affected by this fix? (yes / no)"
      - If yes: re-present affected steps for validation

   d. Continue from the failed step.

6. **Post-protocol: run verification**

   After all steps have passed (or been explicitly skipped), run the verify skill:

   ```bash
   openspec instructions apply --change "<slug>" --json
   ```

   Then perform the verification checks from `.claude/commands/opsx/verify.md`:
   - **Completeness**: tasks checked off, spec requirements covered, protocol complete
   - **Correctness**: implementation matches spec scenarios
   - **Coherence**: design decisions followed

   Present the verification report.

7. **Handle verification issues**

   If CRITICAL issues are found:
   - Present each issue with its location and recommendation
   - Enter issue resolution mode (same as step 5) for each one
   - After all CRITICAL issues are fixed, re-run verification
   - Repeat until no CRITICAL issues remain

   If only WARNINGs or SUGGESTIONs:
   - Present them and ask: "These are non-critical. Fix now or note them for the PR?"

8. **Report outcome**

   ```
   ## Walk Complete — <slug>

   ### Protocol Steps
   ✓ Step 1.1 — <name>
   ✓ Step 1.2 — <name>
   ⚠ Step 2.1 — <name> (skipped)

   ### Verification
   ✓ Completeness: N/M tasks, all requirements covered
   ✓ Correctness: all scenarios addressed
   ✓ Coherence: design decisions followed

   Ready to ship. Run `/opsx:ship <slug>` to finalize.
   ```

   Or if issues remain:
   ```
   ⚠ Walk complete with notes. See issues above before shipping.
   ```

**Guardrails**
- Never skip a `<!-- HUMAN CHECKPOINT -->` step without explicit developer confirmation
- Never modify spec files without developer confirmation
- After any code fix, always offer to re-check affected earlier steps
- Do not proceed to `/opsx:ship` — that is the developer's explicit action
- If protocol.md is missing checkboxes (plain text steps), warn but still walk through them
