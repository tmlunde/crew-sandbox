# Contributing to crew-sandbox

Several test agents share this repo. These few rules keep their work
consistent and easy for the owner to review.

Work only on tasks the owner has approved. One task, one branch, one
pull request.

## Branch names

Branch off `main`. Name the branch after the task:

```
<task-id>-<short-topic>
```

- Lowercase, words joined by hyphens.
- Start with the task id, e.g. `pho-3-contributing`, `pho-1-overview`.
- Keep the topic to two or three words.

Never commit straight to `main`.

## Commit messages

```
<Verb> <what changed> (<TASK-ID>)

Optional body: why the change was made, wrapped at about 72 columns.
```

- First line: imperative mood ("Add", "Fix", "Update"), under 72
  characters, no trailing period, task id in brackets at the end.
- Example: `Add CONTRIBUTING.md with branch and commit rules (PHO-3)`
- Keep each commit to one idea. Small commits are easier to review.
- Never commit secrets (`.env`, keys, tokens, local settings files).

## Pull requests

Open one pull request per task, against `main`. It should include:

- **Title:** same style as a commit's first line, with the task id.
- **What changed:** a few plain sentences.
- **Why:** the task it comes from, and the problem it solves.
- **How to check:** the steps the owner can follow to see it works.
- **Done-when:** each line from the task, with how it is met.

Keep the PR small and limited to the task. Ideas outside it go to
the owner as a new task proposal, not into the same PR.

The owner reviews and merges. Agents do not merge their own PRs.
