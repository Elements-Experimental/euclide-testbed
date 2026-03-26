---
name: "OPSX: Spec Review"
description: Interactively review spec artifacts, surface grey areas and open questions, and resolve them with the developer
category: Workflow
tags: [workflow, spec, review]
---

Review the spec artifacts for a change, identify ambiguities and open questions, and interactively resolve them with the developer.

Use this after a spec PR has been opened (and before it is merged) to ensure the spec is well-defined before implementation begins.

**Input**: Optionally specify a change slug (e.g., `/opsx:spec-review 42-add-auth`). If omitted, infer from current branch or prompt.

**Steps**

1. **Select the change**

   If a slug is provided, use it. Otherwise:
   - Infer from current branch: strip `spec/` or `feat/` prefix
   - If ambiguous, run `openspec list --json` and use **AskUserQuestion** to select

   Always announce: "Reviewing specs for change: `<slug>`"

2. **Read all spec artifacts**

   Read the following files from `openspec/changes/<slug>/`:
   - `proposal.md` — why and what
   - `specs/*/spec.md` — all spec files (requirements and scenarios)
   - `design.md` — if present

3. **Identify grey areas and open questions**

   For each artifact, look for:
   - Vague or ambiguous requirements (no clear pass/fail criteria)
   - Requirements missing scenarios (at least one scenario per requirement)
   - Scenarios with unclear GIVEN/WHEN/THEN conditions
   - Implicit assumptions not made explicit
   - Out-of-scope items not listed
   - Design decisions not yet made (open questions in design.md)
   - Conflicting requirements across spec files
   - Missing edge cases in scenarios

   Build a list of issues, each with:
   - Location: `specs/<capability>/spec.md § Requirement: X`
   - Type: Grey area / Missing scenario / Open question / Ambiguity / Conflict
   - Description: what is unclear and why it matters for implementation

4. **Present issues to developer**

   Group by severity:
   - **Must resolve** (blocks implementation): missing scenarios, conflicting requirements, ambiguous pass/fail criteria
   - **Should resolve**: open questions, implicit assumptions
   - **Consider adding**: edge cases, non-goals clarification

   For each issue, use **AskUserQuestion** (or ask inline) to resolve it:
   - Present the issue with its location
   - Propose options or ask for the developer's decision
   - Wait for the answer before moving to the next issue

5. **Update artifacts with resolutions**

   For each resolved issue:
   - Edit the relevant artifact file with the clarification
   - Add missing scenarios using the Given/When/Then format
   - Add edge cases to existing scenarios
   - Add open questions to a `## Open Questions` section if not yet resolved (mark as `[ ]` unresolved, `[x]` resolved)

   Commit changes:
   ```bash
   git add openspec/changes/<slug>/
   git commit -m "spec(<slug>): resolve grey areas from spec review"
   ```

6. **Generate review summary**

   Output a summary for the spec PR comment (or for the developer to paste):
   ```
   ## Spec Review Summary

   **Change:** <slug>
   **Reviewed:** <list of files reviewed>

   ### Resolved
   - <issue 1>: <resolution>
   - <issue 2>: <resolution>

   ### Still Open
   - <issue 3>: awaiting <decision from whom>

   ### Ready for implementation: Yes / No (pending: <list>)
   ```

**Guardrails**
- Do not invent requirements — only clarify existing ones or add missing scenarios for existing requirements
- Spec adjustments must be confirmed by the developer before being written
- If the developer decides a grey area is intentional (e.g., implementation-defined), note it explicitly in the spec as an open question or as a non-requirement
- Push changes only after all resolutions have been reviewed by the developer
