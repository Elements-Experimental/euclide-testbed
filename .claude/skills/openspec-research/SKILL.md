---
name: openspec-research
description: Investigate the codebase (and ecosystem, for greenfield/new-tech changes) for an OpenSpec change and produce research.md. Documents existing patterns, integration points, reusable assets, risks, and — when relevant — ecosystem findings with confidence levels. Run before design work begins.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: euclide
  version: "1.0"
---

Investigate the codebase and produce `research.md` for the change.

**Input**: A change name. If omitted, infer from current branch or prompt.

---

**Steps**

1. **Select the change**

   If a name is provided, use it. Otherwise infer from the current branch (strip the branch type prefix — everything up to and including the first `/`). If ambiguous, run `openspec list --json` and use AskUserQuestion.

   Always announce: "Researching codebase for change: `<name>`"

2. **Load change context**

   Read the change's existing artifacts to understand what is being built:
   - `openspec/changes/<name>/proposal.md` — what is changing and why
   - `openspec/changes/<name>/specs/*/spec.md` (all spec files) — what the system should do

   From these, extract:
   - The capabilities being added or modified
   - The affected system areas (UI, API, data layer, config, etc.)
   - Any existing specs or capabilities referenced

   **Do not skip this step.** Research without understanding what is being built produces irrelevant findings.

3. **Orient in the codebase**

   Read project-level context:
   - `AGENTS.md` — repo conventions, key paths, patterns
   - `openspec/config.yaml` — tech stack and project context

   Identify the **primary areas** this change will touch based on the proposal/specs.

4. **Ecosystem research (conditional)**

   Check whether any trigger condition applies:
   - **Greenfield**: the codebase has no relevant existing code for this change
   - **New technology**: the proposal introduces a library or tool not currently in the project
   - **Tech-choice decision**: the proposal involves choosing between approaches or tools

   If **no trigger applies**, skip to step 5.

   If a trigger applies, use WebSearch and WebFetch to investigate:
   - **Ecosystem patterns**: search for how the community solves this specific problem (e.g. "React infinite scroll accessible 2024", "Python background job queue comparison")
   - **Official docs**: WebFetch the documentation for any library being introduced or considered
   - **Don't hand-roll scan**: does a well-adopted library already solve the core problem? Prefer citing it over re-implementing
   - **Known pitfalls**: community-documented gotchas, breaking changes, or sharp edges for the chosen approach

   Confidence model for external findings:
   - **Confident** — official documentation (WebFetch of the library's own docs site)
   - **Likely** — multiple independent credible sources aligned
   - **Unclear** — single blog post, conflicting sources, or no clear consensus

   Every external finding MUST cite a URL. "Pattern described at https://..." is a finding. "Community generally uses X" is not.

   **Guardrail**: do not pad research.md with generic ecosystem notes for brownfield changes where the codebase already shows clear patterns. If in doubt, skip — codebase evidence beats web evidence.

5. **Investigate systematically**

   For each area identified in step 3:

   a. **Locate files** — use Glob and Grep to find relevant files. Cast wide first, then narrow.
      ```bash
      # Example: find files matching a pattern
      find src/ -name "*.ts" | xargs grep -l "keyword" 2>/dev/null
      ```

   b. **Read them** — read the actual source. Do NOT describe what you expect to find; read it and report what is there.

   c. **Document with citations** — every finding needs a file path. "Pattern found at `src/auth/session.ts:42`" is a finding. "Auth likely uses sessions" is not.

   d. **Classify confidence**:
      - **Confident** — you read the code; it clearly shows this
      - **Likely** — reasonable inference from patterns you read; not directly verified
      - **Unclear** — the code is ambiguous, or you couldn't find it; design.md must resolve this

   **Investigation targets**:

   - **Codebase Context**: Which existing files and modules are directly involved? What is the current state of the code being changed?
   - **Patterns and Conventions**: How does this codebase handle similar concerns? (state management, API calls, error handling, testing patterns, file naming, module structure)
   - **Integration Points**: Where will new code connect to existing code? Entry points, shared types, event handlers, data flows. Flag any that look risky or require changes to existing APIs.
   - **Reusable Assets**: What utilities, components, helpers, constants, or types already exist that should be used instead of re-implemented?
   - **Risks and Unknowns**: What could make implementation harder than expected? Where is the evidence thin? What decisions must be made before tasking?

   **Anti-Stall Guard**: If you make 5 or more consecutive read/search actions (Read, Grep, Glob, Bash) without writing anything, STOP. State in one sentence why you haven't written yet. Then either write what you have, or report "blocked" with the specific information still missing.

6. **Write research.md**

   Get the output path from the schema:
   ```bash
   openspec instructions research --change "<name>" --json
   ```
   Use the `outputPath` and `template` from the JSON response.

   Write research.md following the template structure. Apply these rules:
   - Every finding MUST cite at least one file path as evidence
   - Classify each item: Confident / Likely / Unclear
   - "I couldn't find X — searched `src/` with `grep -r 'keyword'`" is a valid and valuable finding
   - Do NOT describe files you haven't read
   - Be prescriptive: "Use X" not "Consider X or Y" when evidence supports a clear choice
   - Surface "Unclear" items explicitly — they are inputs to design.md, not failures

7. **Confirm and show status**

   ```bash
   openspec status --change "<name>"
   ```

   Report:
   - ✓ research.md written
   - Key findings summary (3–5 bullets)
   - Any "Unclear" items that design.md must resolve
   - What artifact is now unlocked (typically `design`)

---

**Confidence levels**

| Level | Meaning | Example |
|-------|---------|---------|
| **Confident** | Read the code; it clearly shows this | "Auth tokens stored in `src/auth/store.ts` — read line 14" |
| **Likely** | Reasonable inference from patterns read, not directly verified | "Error handling likely follows the pattern in `src/api/users.ts`" |
| **Unclear** | Ambiguous or not found; design.md must resolve | "Could not find how the config is loaded — searched `src/config/`; no initializer found" |

"Unclear" items are not failures — they are the most valuable output. They tell the design author exactly where decisions are needed.

---

**Guardrails**
- Read the codebase — do not invent findings from training-data assumptions
- Cite file paths for every codebase finding — no path = no claim
- Cite URLs for every ecosystem finding — no URL = no claim
- If a file or pattern doesn't exist, state it explicitly (absence is a finding)
- Do NOT run ecosystem research for brownfield changes with clear codebase patterns — skip step 4
- Do NOT produce design decisions or task breakdowns — this skill produces research only
- Do NOT pad findings — a short, accurate research.md is better than a long, speculative one
- Anti-stall: after 5 consecutive reads without writing, write what you have or report blocked
