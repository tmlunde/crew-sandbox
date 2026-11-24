# Contributing to crew-sandbox

Several agents commit here. These two rules keep their work
looking the same, so the owner can review it quickly.

## Branch names

Name a branch `type/short-name`.

The type is one of these four:

| Type     | Use it for                          |
| -------- | ----------------------------------- |
| `docs/`  | docs, such as the README            |
| `feat/`  | something new                       |
| `fix/`   | a fix for something that is wrong   |
| `chore/` | upkeep that changes no behaviour    |

The short name is a few lowercase words joined by hyphens.

Example:

```sh
git switch -c docs/contributing
```

## Commit messages

Write one line, under 72 characters.
Start it with a verb in the imperative: Add, Fix, Remove, Update.
Do not end it with a full stop.

Example:

```sh
git commit -m "Add CONTRIBUTING.md with branch and commit rules"
```

## Handing in

Do not push, and do not open a pull request.
Hand in the branch name and the full commit id (`git rev-parse HEAD`).
Crew shows your commit to the owner, then pushes it once they approve.
