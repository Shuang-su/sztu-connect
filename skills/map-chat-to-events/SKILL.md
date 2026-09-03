---
name: map-chat-to-events
description: Map a lawfully obtained, user-selected chat export into SZTU Connect chat JSONL, Sources, and candidate Events while preserving message IDs, time uncertainty, and reply links. Use for chat-history material; this instruction-only skill does not decrypt databases or provide an automatic platform parser.
---

# Map chat material

1. Work in a user-selected SZTU Connect clone with the pinned local CLI available; if the environment is missing, follow `docs/GETTING_STARTED.md` first. Read `docs/CHAT_IMPORT.md`. Inventory the original through `sztu-connect ingest`; do not decrypt, execute, modify, or publish it.
2. Map selected messages to `schemas/chat-message.schema.json`. Preserve display names when relevant and lawful; do not anonymize by default.
3. Validate with `sztu-connect validate-chat <file> --json`. Rendering is optional and writes only under `.work/`.
4. Create a Source record for the selected export or excerpt. Use message IDs as Citation locators.
5. A statement in chat remains a source statement. Create an Event Claim with the appropriate `memory`, `allegation`, `uncertain`, or `fact` kind; do not promote it to fact merely because multiple messages repeat it.
6. Link the candidate Event to existing Nodes only when identity is clear.
