# crew-sandbox — Overview

## What it is

`crew-sandbox` is a throwaway repository used by Crew's test agents.
Its README says so in one line: "Throwaway repo for Crew's test agents".

It holds no product code. Its job is to give agents a safe place to
practise real work — reading, writing files, branching, opening pull
requests — without any risk to a live project.

## How it's laid out

The repo is almost empty. As of this overview it has one commit
(`e4afe78 Initial commit`) on `main`, and these files:

```
crew-sandbox/
├── README.md     # One-line description of the repo
└── OVERVIEW.md   # This page
```

- **No source code, tests, build files, or CI.** There is nothing to
  install or run.
- **No dependencies or config** (no `package.json`, no lockfiles, no
  `.github/` folder).
- **Default branch:** `main`. Remote: `github.com/tmlunde/crew-sandbox`.

## How to work in it

- Treat anything here as disposable. Nothing depends on it.
- Still work the normal way: branch off `main`, commit, open a pull
  request. That keeps the practice runs close to real ones.
- Keep each change small and tied to one approved task.

## Open gaps

- No shared place yet for design work (screens, sketches, notes).

These are the kind of things a first follow-up task could add.
