# crew-sandbox

Throwaway repo for Crew's test agents.

## What it is for

Agents practise real work here: reading files, writing them,
committing on a branch, and handing the work in.
Nothing here ships, so a mistake costs nothing.

There is no code, no build, no tests and no setup step.

## Who works here

Crew's agents do the work. The owner decides what gets done.

An agent works only on a task the owner has approved.
If an agent has a new idea, it proposes a task and waits for a yes.

## How to hand in work

1. Make a branch in your own copy of the repo.
2. Do the work and commit it on that branch.
3. Hand in the task with the branch name and the full commit id
   (`git rev-parse HEAD`).

Do not push, and do not open a pull request.
Crew shows your commit to the owner.
Once the owner approves, Crew pushes it and opens the pull request.
The owner closes the task, not the agent.

## More

See [OVERVIEW.md](OVERVIEW.md) for how the repo is laid out.
