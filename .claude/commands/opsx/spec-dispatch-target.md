<!--
  NOT a user-invocable slash command.
  This file is the agent prompt pasted verbatim into spec-agent issue bodies by CI (ready-to-dev.yml)
  and by /opsx:dispatch-spec. It instructs the coding agent that picks up the spec-agent issue.
-->

## Spec agent instructions

You are a spec creation agent. Your job is to generate the OpenSpec artifacts for this change and open a spec PR for human review.

**Your change slug is ``.**
**Feature branch: `feat/`**
**Product issue: #**

### What you need to do

1. **Check out the feature branch**
   ```bash
   git checkout feat/
   ```

2. **Create the spec branch**
   ```bash
   git checkout -b spec/
   ```

3. **Generate spec artifacts**

   Run `/opsx:propose ` (`.claude/commands/opsx/propose.md`) to generate all artifacts under `openspec/changes//`:
   - `proposal.md` — why and what
   - `specs/<capability>/spec.md` — requirements and scenarios
   - `design.md` — technical approach (only if needed)
   - `tasks.md` — implementation checklist

   Alternatively, follow the skill at `.claude/skills/openspec-propose/SKILL.md` if running in an environment without slash commands.

   Base the artifacts on:
   - The product issue body (#) — user story and acceptance criteria
   - Any linked design assets (Figma, etc.) mentioned in the issue
   - Existing specs in `openspec/specs/` — check for capabilities to extend vs. create new

4. **Add a grey areas section to the PR body**

   In the PR description, add a **## Grey Areas & Open Questions** section listing:
   - Any ambiguous acceptance criteria from the product issue
   - Requirements where the expected behavior is unclear
   - Scenarios where edge cases need human input
   - Technical decisions deferred to design

5. **Commit and open the spec PR**

   ```bash
   git add openspec/changes//
   git commit -m "spec(): add change artifacts"
   git push -u origin spec/
   gh pr create \
     --head spec/ \
     --base feat/ \
     --title "spec: " \
     --label "spec" \
     --body "$(cat openspec/changes//proposal.md)

   ---

   ## Grey Areas & Open Questions
   <!-- list grey areas here -->
   "
   ```

### Guardrails

- Base the spec PR on `feat/`, NOT on `main` or `dev`
- Do not implement any code — spec artifacts only
- Every requirement MUST have at least one scenario in Given/When/Then format using `####` headers
- Do not close or merge the PR — a human will review it first
