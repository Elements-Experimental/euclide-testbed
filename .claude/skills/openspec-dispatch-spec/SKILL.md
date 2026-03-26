---
name: openspec-dispatch-spec
description: Manually dispatch the spec creation task for a change — creates feat/ branch, writes .meta, creates spec-agent issue, links as sub-issue. Use when ready-to-dev CI didn't trigger or to re-dispatch.
license: MIT
compatibility: Requires gh CLI authenticated and git remote access.
metadata:
  author: euclide
  version: "1.0"
---

Manually trigger spec creation for a change.

**Input**: Optionally specify a change slug or issue number. If omitted, prompt for the source issue.

**Steps**

1. **Resolve the source issue and slug**

   If a numeric argument is given, treat it as an issue number — fetch the title via:
   ```bash
   gh issue view <N> --json number,title
   ```
   Derive the slug: `<number>-<title-slug>` (lowercase, hyphens, truncate title at 50 chars).

   If a full slug is given (starts with digits and contains a hyphen), use it directly.

   If nothing is given, use AskUserQuestion to ask for the issue number or URL.

   Always announce: "Using slug: `<slug>`"

2. **Create feat/ branch if needed**

   ```bash
   git ls-remote --exit-code --heads origin feat/<slug>
   ```

   If the branch does not exist: create it off the default branch, write `openspec/changes/<slug>/.meta` with `product_issue=<N>`, commit, and push.

   If the branch already exists: verify `.meta` is present. If missing, write it.

3. **Ensure labels exist**

   ```bash
   gh label create "spec-agent" --color "e4e669" --description "Spec creation task for an AI agent" || true
   ```

4. **Check for existing spec-agent issue**

   ```bash
   gh issue list --label "spec-agent" --state open --search "spec: <slug> in:title" --json number,url
   ```

   If one exists: report its URL and skip creation.

5. **Create spec-agent issue**

   Body must include: slug, feature branch, source issue link, step-by-step instructions (check out feat/, create spec/, run propose, add grey areas section, open spec PR to feat/ with label `spec`), reference to `.claude/commands/opsx/spec-dispatch-target.md` and `.claude/skills/openspec-propose/SKILL.md`.

6. **Link as sub-issue**

   ```bash
   gh api repos/<owner>/<repo>/issues/<issue-number>/sub_issues \
     --method POST \
     --field sub_issue_id=<spec-agent-issue-number>
   ```

   Warn if API unavailable (plan limitation).

7. **Comment on source issue** with link to spec-agent issue.

8. **Report outcome**: spec-agent issue URL, feature branch, next step.

**Guardrails**
- Do not create the spec-agent issue if one already exists with the same title
- Use `product_issue=<N>` format in `.meta`
