---
name: openspec-spec-review
description: Interactively review spec artifacts for a change, surface grey areas and open questions, and resolve them with the developer before implementation begins.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: euclide
  version: "1.0"
---

Review the spec artifacts for a change, identify ambiguities, and interactively resolve them with the developer.

**Input**: Optionally specify a change slug. If omitted, infer from current branch or prompt.

**Steps**

1. **Select the change**

   If a slug is provided, use it. Otherwise infer from current branch (strip the branch type prefix — everything up to and including the first `/`). If ambiguous, run `openspec list --json` and use AskUserQuestion.

   Always announce: "Reviewing specs for change: `<slug>`"

2. **Read all spec artifacts**

   Read: `openspec/changes/<slug>/proposal.md`, `openspec/changes/<slug>/specs/*/spec.md` (all files), `openspec/changes/<slug>/design.md` if present, and `openspec/changes/<slug>/research.md` if present.

3. **Structured analysis**

   **Assumption audit** — for each implicit assumption in the specs, surface it in this format:
   - **Assumption**: what the spec assumes to be true
   - **Evidence**: what in the spec artifacts (proposal/spec/design/research) or, if you inspect it, the codebase supports this. Cite concrete locations: for specs, use file paths and section headings (e.g., `openspec/changes/<slug>/specs/api/spec.md#Error handling`); for code, use real code file paths.
   - **Consequence**: what breaks if the assumption is wrong
   - **Confidence**: Confident | Likely | Unclear

   **Spec-level checks** — for each artifact, look for:
   - Vague or ambiguous requirements (no clear pass/fail criteria)
   - Requirements missing scenarios
   - Scenarios with unclear GIVEN/WHEN/THEN conditions
   - Missing out-of-scope items
   - Conflicting requirements

   **Implementation feasibility** — informed by research.md (if present):
   - Do the specs assume integration points that research flagged as risky?
   - Are there "Unclear" items in research.md that the specs haven't resolved?
   - Are spec requirements feasible given the existing codebase patterns?

4. **Present issues to developer**

   Group by severity: Must resolve / Should resolve / Consider adding.

   For each issue, use AskUserQuestion to get a resolution before moving on.

5. **Update artifacts with resolutions**

   Edit affected files, add missing scenarios, clarify requirements. Commit:
   ```bash
   git add openspec/changes/<slug>/
   git commit -m "spec(<slug>): resolve grey areas from spec review"
   ```

6. **Generate review summary** for the PR (resolved items, still-open items, ready status).

**Guardrails**
- Do not invent requirements — only clarify or add scenarios for existing ones
- All spec changes require developer confirmation before writing
