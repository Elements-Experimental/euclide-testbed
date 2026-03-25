# euclide-testbed — Agent Guidelines

## Reference

| Resource | Purpose |
|---|---|
| `docs/reference/commands.md` | Full `/opsx:*` command reference |
| `docs/reference/branch-workflow.md` | End-to-end branch and issue workflow |

## Repo map

| Path | Purpose |
|---|---|
| `openspec/specs/` | Domain specs — source of truth for requirements |
| `openspec/changes/` | Active and archived OpenSpec changes |
| `docs/adr/` | Architecture Decision Records |
| `docs/architecture.md` | Tech stack and high-level design |
| `docs/testing.md` | Test and lint commands |

## Conventions

- **Branches:** `feat/<slug>` for implementation; `spec/<slug>` for spec authoring; `fix/<issue-number>-<slug>` for standalone fixes
- **Commits:** `type(#N): description` — omit the number only if no issue exists; types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`
- **PR title:** `feat: <slug>` for OpenSpec-driven work; `type(#N): description` for others
- **Integration branch:** `dev` — all feature branches merge here

## Development process

1. Read the change directory (`openspec/changes/<slug>/`) and all linked docs in full
2. **Test-driven:** write or update tests before implementing
3. Implement the task
4. Run all automated tests (`docs/testing.md`) — not done until they pass
5. Update relevant docs; if none fit, add one
6. Commit: `type(#N): description` — use the issue number from the issue body; do not invent one
7. Update the task checkbox to `[x]` immediately after completing each task
8. On the final task: archive with `/opsx:archive` (`.claude/commands/opsx/archive.md`)
9. If blocked at any point: open a draft PR immediately with a clear blocker description

## Archive is part of the task

A change is not complete until it has been archived. Run `/opsx:archive` (`.claude/commands/opsx/archive.md`) on the final task — this is a completion requirement, not an optional step. Do not consider the task done, open a PR for review, or close the issue unless the change directory has been moved to `openspec/changes/archive/`.

## Documentation and tests are part of the task

Any change must be accompanied by updated documentation (specs, `docs/`, `README.md`,`AGENTS.md`, or whatever is relevant) in the same commit or PR — not as a follow-up. Tests must be written for every change, covering all acceptance criteria and edge cases. If a case genuinely cannot be automated, state it explicitly in the PR's "Test protocol" section with a reason.

## Guardrails

- Keep changes minimal — only touch files required by the task
- No follow-up commits to fix issues that should have been caught before committing

## Tech stack

Python
