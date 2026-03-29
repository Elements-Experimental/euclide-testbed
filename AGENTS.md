# euclide-testbed — Agent Guidelines

## Repo map

| Path | Purpose |
|---|---|
| `openspec/specs/` | Domain specs — source of truth for requirements |
| `openspec/changes/` | Active and archived OpenSpec changes |
| `docs/adr/` | Architecture Decision Records |
| `docs/architecture.md` | Tech stack and high-level design |
| `docs/testing.md` | Test and lint commands |

## Conventions

- **Branches:** The integration branch `<type>/<slug>` is created by the workflow when an issue is labeled `ready: feat`, `ready: fix`, `ready: chore`, or `ready: docs` — do not push here directly. Use `spec-<slug>` (or `<agent>/spec-<slug>`) for spec authoring; `implem-<slug>` (or `<agent>/implem-<slug>`) for implementation. Both PR into the integration branch.
- **Commits:** `type(#N): description` — use the **product issue number** from `openspec/changes/<slug>/.meta`; the `type` matches the integration branch prefix (`feat`, `fix`, `chore`, `docs`); omit the number only if no issue exists
- **PR titles:** `spec: <slug>` for spec PRs; `implem: <slug>` for implementation PRs; integration PR title is `<type>: <slug>`
- **Integration branch:** `dev` — all feature branches merge here

## Development process

1. Read the change directory (`openspec/changes/<slug>/`) and all linked docs in full
2. **Test-driven:** write or update tests before implementing
3. Implement the task
4. Run all automated tests (`docs/testing.md`) — not done until they pass
5. Update relevant docs; if none fit, add one
6. Commit: `type(#N): description` — use the issue number from the issue body; do not invent one
7. Update the task checkbox to `[x]` immediately after completing each task
8. On the final task: write `openspec/changes/<slug>/protocol.md` (see below), then open a draft PR to `feat/<slug>`
9. If blocked at any point: open a draft PR immediately with a clear blocker description

## Writing protocol.md

After all tasks are complete, write the test protocol at `openspec/changes/<slug>/protocol.md` using the template at `openspec/schemas/elements-impact/templates/protocol.md`.

- Group steps by feature area
- **Automation-first**: only use `<!-- HUMAN CHECKPOINT -->` for steps requiring human judgment (visual rendering, interactive UX, auth flows, external services). Automated checks (tests, lint, type checking) are run by `/opsx:walk` automatically before the walkthrough — do not include them as manual steps.
- Each step should include a `- **Built**: <one sentence>` line before the action, so the developer has context for why they're checking it
- Each step MUST have a concrete action and an **Expected** result
- Link steps to spec scenarios where applicable: `_(AC: specs/<capability>/spec.md § Scenario: X)_`
- Use `- [ ]` checkboxes — **do not pre-check them**; the developer runs the protocol, not the agent

## Archiving is done by the developer

**Do not run `/opsx:archive`** — archiving happens after the developer has run `/opsx:walk` and verified the implementation. The developer runs `/opsx:ship` to archive, squash commits, and open the final PR.

## Documentation and tests are part of the task

Any change must be accompanied by updated documentation (specs, `docs/`, `README.md`, `AGENTS.md`, or whatever is relevant) in the same commit or PR — not as a follow-up. Tests must be written for every change, covering all acceptance criteria and edge cases. If a case genuinely cannot be automated, state it explicitly in the PR's "Test protocol" section with a reason.

## When things go wrong

Debugging is a scientific process. Apply it consistently:

1. **Observe** — read the actual error message and stack trace in full. Do not paraphrase it.
2. **Hypothesize** — form one specific, falsifiable hypothesis about the cause. "I think X because Y."
3. **Test one thing** — make the smallest possible change that would confirm or refute the hypothesis. Do not change multiple things at once.
4. **Conclude** — did the change help? If yes, root cause found. If no, discard hypothesis and return to step 2 with new evidence.

**Stop after 3 failed attempts.** If three distinct hypotheses have all been tested and disproved, you are missing context. Open a draft PR with a clear description of: what you observed, the three hypotheses you tested, what you found, and what information you need. Do not keep trying random fixes.

**Do not restart** — do not wipe state, re-clone, or start over as a debugging strategy. Restarts hide evidence.

## Working philosophy

- **Treat knowledge as hypothesis.** Training data is stale. What you "know" about a library or pattern may be outdated. Verify against the actual codebase before asserting.
- **Cite evidence.** When describing how something works, reference the file path. "Based on `src/auth/session.ts:42`" is useful. "I believe the auth system uses JWT" is not.
- **Be prescriptive.** Say "use X" not "consider X or Y." When evidence supports a clear choice, make it. Reserve "could go either way" for genuinely ambiguous cases.
- **Surface uncertainty explicitly.** "I'm not sure where the config is loaded — I found `config/defaults.ts` but couldn't confirm it's the active path" is more useful than a confident wrong answer.
- **Read before concluding.** Do not describe file contents you haven't read. Do not assert a pattern exists without finding it.

## Guardrails

- Keep changes minimal — only touch files required by the task
- No follow-up commits to fix issues that should have been caught before committing

## Tech stack

Markdown
