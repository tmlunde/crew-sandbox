# Working rules for agents

How agents work in `crew-sandbox`. Keep changes small and easy to check.

## Branches

- Never commit straight to `main`.
- Start every change from an up-to-date `main` on a new branch.
- Name it `<type>/<short-topic>`, lowercase words joined with hyphens:
  - `feat/` new content or behaviour
  - `fix/` a correction
  - `docs/` documentation only
  - `chore/` housekeeping (config, cleanup)
- Example: `docs/agent-working-rules`.
- One task per branch.

## Commits

- Subject line: `<type>: <what changed>`, using the same types as branches.
  Use the imperative mood, 72 characters at most, and no full stop at the end.
  - Example: `docs: add agent working rules`
- If the reason isn't obvious, add a body after a blank line that says why.
- Each commit covers one change. Stage only the files that change touches,
  never everything with `git add -A` or `git add .`.
- Never commit secrets, local config or editor files.

## Pull requests

- Every change reaches `main` through a pull request. There are no direct
  pushes.
- Use the commit subject as the PR title.
- The PR body says what changed, why, and how to check it, and names the task
  it belongs to (for example `PHO-5`).
- The repo has no CI, so the diff is the proof. Keep it small enough to
  review in one read.
- Merge only after the owner has reviewed it.
