# Deploy plan

**Nothing is deployed from crew-sandbox.**

This is a test-only repo for Crew's agents. It has no app code and no
deploy config, and nothing from it runs on any server.

## What post-deploy checks should expect

- Servers for crew-sandbox: **none**.
- If a check finds anything running for crew-sandbox, that is drift.
  Report it to the owner.

## Changing this plan

If crew-sandbox ever needs to run something, the owner decides first.
Then this file is updated to say what runs where, in the same change.

Agreed with the owner on 2026-11-24 (PHO-16).
