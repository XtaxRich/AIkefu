# 00 Repo Policy

## Current stage
The main branch is used as a thesis and system-design documentation center.

## Why the first code scaffold is removed
The first `src/` and `tests/` version only provided placeholders. It did not define:
- full policy graph schema
- action authorization rules
- trace schema
- replay and scoring
- experience update loop
- experiment contracts

Because of that, the first code version is not used as the official baseline.

## What should stay in main
- research question
- literature matrix
- architecture and module specs
- data contracts
- evaluation protocol
- experiment plan
- module handoff

## What should not go into main now
- toy demo code
- black-box scripts without trace
- prompt-only logic without contracts
- code without matching design docs

## Merge gate for future code
Any future implementation merged into `main` should have:
1. a matching module brief
2. input/output contracts
3. minimal evaluation cases
4. trace design
5. failure-path notes
