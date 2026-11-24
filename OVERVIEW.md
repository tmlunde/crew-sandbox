# crew-sandbox: overview

What I found on 2026-11-24, looking at `main` at commit `e4afe78`.

## What it is

`crew-sandbox` is a throwaway repo where Crew's test agents work. The README
says so: "Throwaway repo for Crew's test agents". There is no application,
service or deployable thing in it yet.

## How it's laid out

```
crew-sandbox/
├── README.md     # two lines: the repo name and its purpose
└── OVERVIEW.md   # this file
```

- One branch, `main`, which tracks `origin/main`.
- One commit, `e4afe78` "Initial commit" (2026-11-18), which adds `README.md`.
- No source code, build files, tests, CI config, `.gitignore` or license.

## What runs where

Nothing. There are no deploy configs, Dockerfiles, infrastructure files or
service definitions, so nothing in this repo runs on any server.

## Notes for agents working here

- Each agent's working copy also holds runtime dotfiles (`.claude/`,
  `.mcp.json`, `.bashrc`, `.gitconfig`, `.idea`, `.vscode` and others). They
  come from the agent sandbox, not the repo, and they are untracked. Don't
  commit them. The repo has no `.gitignore`, so `git add -A` would stage them.
- Keep changes on a branch. Don't commit to `main` directly.
