---
name: setup-sztu-connect
description: Set up, initialize, resume, or check a local SZTU Connect working copy before recording campus history. Use when a user wants to start using the project, prepare its environment and applicable bundled tools, or recover an interrupted setup. This workflow does not import personal records or publish anything.
---

# Set up SZTU Connect

Locate the user's working copy or the folder they selected for it. An installed plugin cache is not their archive. Do not overwrite an unrelated directory, an existing environment, or uncommitted files; do not install all Agent clients.

Read the shared [getting-started guide](../../docs/GETTING_STARTED.md) in full. If the skill was installed without the guide, read `https://raw.githubusercontent.com/Shuang-su/sztu-connect/main/docs/GETTING_STARTED.md`, then obtain the user checkout as directed there. After selecting the checkout, read its root `AGENTS.md` and local guide; use that checkout's scripts and existing state.

Follow the guide's environment detection, tool preparation, isolated example and recovery flow. Confirm the shell operates on the selected local workspace before installing anything. Reuse a valid environment and run the helper with an explicit absolute `--root`; use `--check --json` for a check-only request. Do not use a client's `/init` to rewrite project instructions.

The helper handles repeatable project-local preparation. The Agent handles official system installers, normal application installation and user authorization as described in the guide. An installer file alone is not an installed application. If the registry or platform artifact is missing, report that dependency without substituting another tool or claiming completion.

Read each stage's status, not only the exit code. Distinguish a usable local core from pending tools, and distinguish installed-app metadata from an actual launch test. Open or link the generated example results, report the working-copy location and outstanding user actions, then ask what first campus event the user wants to record.

Only continue into GitHub setup when the user asks to synchronize or contribute. Initialization does not authorize account login, remote changes, push, PR, merge, chat-history reading, Computer History capture or original-material import.
