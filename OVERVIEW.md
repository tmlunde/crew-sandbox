# crew-sandbox overview

## What this repo is

crew-sandbox is a throwaway repo for Crew's test agents.
That is what the README says, and it is all the repo holds today.

Agents use it to practise real work: reading code, writing files,
committing on a branch, and handing the work in. Nothing here ships.
Breaking or rewriting things here costs nothing.

## How it is laid out

```
crew-sandbox/
├── README.md     # one line: what the repo is for
└── OVERVIEW.md   # this file
```

There is no source code. There is no build, no tests, no dependencies,
and no setup step. If you can clone it, you can use it.

The history is one commit, `e4afe78 Initial commit`. It adds `README.md`.
The default branch is `main`.

## How work lands here

1. The owner approves a task.
2. An agent does the work on a branch in its own copy of the repo.
3. The agent commits and hands in the branch and commit.
4. The owner reviews it. Crew pushes it and opens the pull request.

Agents do not push or open pull requests themselves.

## What is missing

- The README does not say who may change the repo, or how.
- There are no rules on branch names or commit messages.

These gaps are small, but they matter once more than one agent works here.
