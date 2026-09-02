---
name: fact-check-event
description: Trace SZTU Connect event claims to source locators, compare support and counterevidence, check time and identity uncertainty, and produce a fact-check matrix. Use for 核查, 纠错, 争议, duplicate-event, or provenance questions; remain read-only unless the user asks to apply corrections.
---

# Fact-check an event

1. Work in a user-selected SZTU Connect clone with the pinned local CLI installed as described in `README.md`. Read the Event, every cited Source, linked Event/Node, and generated backlinks.
2. For each Claim report: text, kind, certainty, Event time, supporting Source locators, contradicting Source locators, independence groups, and unresolved questions.
3. Count only `supports` Citations from different non-empty independence groups as corroboration. Do not count copies, context, counterevidence, OCR, AI summaries, or vector search results as independent sources.
4. Verify that Event-to-Node relationships use the right identity. Similar names or aliases do not prove they are the same person, organization, place, or institution.
5. Preserve conflicting evidence. “Not yet confirmed” is not the same as “disproved.”
6. When asked to apply a correction, edit the smallest Claim/Citation/Link scope, explain the evidence change, rebuild, and keep Git history intact.

Do not assign governance roles or turn a fact-check report into an authority-based publication decision.
