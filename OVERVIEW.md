# crew-sandbox: overview

## What it is

`crew-sandbox` is a throwaway repository where Crew's test agents can practise.
Its README says: *"Throwaway repo for Crew's test agents"*. It has no product
code, no build and no tests. People and agents use it to try out the Crew
workflow (task, branch, commit, hand-in) where mistakes do no harm.

## How it's laid out

Checked on 2026-11-25 at commit `e4afe78` ("Initial commit", the only commit):

```
crew-sandbox/
├── README.md     # the two-line description above
└── OVERVIEW.md   # this file (added by PHO-19)
```

- **Branches:** just `main`.
- **Tracked files:** only `README.md` (2 lines) before this change.
- **No** source folders, `cad/` folder, dependency files, CI config,
  `.gitignore` or licence.
- Any dotfiles you see in an agent's working copy (`.bashrc`, `.mcp.json`,
  `.vscode`, and so on) come from the agent sandbox. They are not tracked by git
  and are not part of the repo.

So there are no conventions to follow yet. Whatever the first real tasks add
will set the layout.

## Suggested next tasks

1. **Add a `cad/` skeleton with one example part.** Add a small parametric
   CadQuery part (for example a wall bracket) with every size as a named number
   at the top, plus a script that exports STEP, STL and a drawing sheet with the
   key dimensions, material and mass.
   *Why:* it sets the layout and the export routine once, so every later part
   task follows the same pattern and the output can be checked the same way.
2. **Add a `.gitignore` and a short "how to work here" section in the README.**
   Say which generated files are committed and which are ignored (for example
   commit STEP and STL, ignore caches and renders), and the branch and commit
   rules.
   *Why:* the repo has neither yet, and agents working in parallel will
   otherwise commit stray files and make inconsistent choices.
