---
name: "OPSX: Dispatch Spec"
description: Manually dispatch the spec creation task — creates feat/ branch, writes .meta, creates spec-agent issue, links as sub-issue
category: Workflow
tags: [workflow, spec, dispatch]
---

Manually trigger spec creation for a change. Use this when the `ready-to-dev.yml` CI workflow didn't fire, or to re-dispatch an existing task.

**Input**: Optionally specify a change slug or issue number/URL (e.g., `/opsx:dispatch-spec 42` or `/opsx:dispatch-spec 42-add-auth`). If omitted, prompt for the source issue.

**Steps**

1. **Resolve the source issue and slug**

   If a numeric argument is given, treat it as an issue number — fetch the title via:
   ```bash
   gh issue view <N> --json number,title
   ```
   Derive the slug: `<number>-<title-slug>` (lowercase, hyphens, truncate at 50 chars).

   If a full slug is given (contains a hyphen and starts with digits), use it directly.

   If nothing is given, use **AskUserQuestion** to ask for the issue number or URL.

   Always announce: "Using slug: `<slug>`"

2. **Create feat/ branch if needed**

   ```bash
   git ls-remote --exit-code --heads origin feat/<slug>
   ```

   If the branch does not exist:
   ```bash
   git checkout -b feat/<slug> origin/dev
   mkdir -p openspec/changes/<slug>
   echo "product_issue=<issue-number>" > openspec/changes/<slug>/.meta
   git add openspec/changes/<slug>/.meta
   git commit -m "chore: initialise change directory for #<issue-number>"
   git push -u origin feat/<slug>
   ```

   If the branch already exists: check out `feat/<slug>` and verify `.meta` exists. If missing, write it.

3. **Ensure labels exist**

   ```bash
   gh label create "spec-agent" --color "e4e669" --description "Spec creation task for an AI agent" || true
   ```

4. **Check for an existing spec-agent issue**

   ```bash
   gh issue list --label "spec-agent" --state open --search "spec: <slug> in:title" --json number,url
   ```

   If one exists: report its URL and skip creation. Ask if the developer wants to add a comment to re-notify.

5. **Create spec-agent issue**

   If none exists:
   ```bash
   gh issue create \
     --title "spec: <slug>" \
     --label "spec-agent" \
     --body "$(cat)"
   ```

   Issue body must include:
   - Change slug and feature branch
   - Link to source issue (`#<issue-number>`)
   - Step-by-step instructions: create `spec/<slug>` off `feat/<slug>`, run `/opsx:propose <slug>`, add grey areas section, open spec PR with label `spec`
   - Reference to `.claude/commands/opsx/spec-dispatch-target.md` for the full agent prompt
   - Reference to `.claude/skills/openspec-propose/SKILL.md` for the propose skill

6. **Link as sub-issue**

   ```bash
   gh api repos/<owner>/<repo>/issues/<issue-number>/sub_issues \
     --method POST \
     --field sub_issue_id=<spec-agent-issue-number>
   ```

   If the API call fails (plan limitation): warn and suggest manual linking.

7. **Comment on source issue**

   ```bash
   gh issue comment <issue-number> --body "Spec task created: #<spec-agent-issue-number>. Assign it to a coding agent or run \`/opsx:dispatch-spec <slug>\` to re-dispatch."
   ```

8. **Report outcome**

   Print:
   - Spec-agent issue URL
   - Feature branch: `feat/<slug>`
   - Next step: "Assign the spec-agent issue to a coding agent, or pull `feat/<slug>` and run `/opsx:propose <slug>` locally."

**Guardrails**
- Fail clearly if `gh` is not authenticated (`gh auth status`)
- Do not push to `feat/<slug>` if only a `.meta` update is needed on a pre-existing branch — just write the file locally and push
- Do not create the spec-agent issue if one already exists with the same title
