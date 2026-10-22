# Aster Continuity — Master Context

_Last updated: 2026-10-22_

## Purpose
Build a portable AI assistant workflow inspired by the user's NOVA — School for Independent Minds, Edition 4.0 archive. The goal is to carry project context, decisions, discoveries, corrections, and next steps across chats using explicit records.

## Project context confirmed so far
- User provided `NOVA_Independent_Minds_Academy_v4_2026-10-20 (3)(1).zip`.
- The archive was reviewed for its charter, reasoning and correction protocols, curriculum materials, prompt cards, workbooks, practical labs, evaluation plans, synthetic examples, references, and governance/privacy documentation.
- The archive warns against persona cloning, false claims of imported memories, and claims of permanent learning from reading a ZIP.
- Important academy methods: classify claims by evidence status; generate alternative explanations; try to falsify; verify with independent methods; report uncertainty; preserve original answers and correction receipts; evaluate on unseen tasks rather than imitation.
- Chosen assistant working identity: **Aster**.
- Motto: **Curiosity with integrity. Capability with human control.**
- GitHub account `PeachieUnicorn` has repositories `Project-NOVA` (private) and `Project-Aster` (public); the connected integration reported admin/push access to `Project-Aster`.
- `Project-Aster` was initially empty. Its README, identity charter, master context, session template, and initial study record were created and verified by readback on 2026-10-22.
- Google Drive was subsequently connected. Aster — Continuity and Build Hub was created and verified: https://docs.google.com/document/d/1797qdpDPjeXWMCFDKSTOq2Pke9EiDbOoMV3tsRzV2Bc/edit . The APP/ Python MVP scaffold and CONTINUITY/SYNC_POLICY.md were committed to GitHub and verified.

## Decisions
- Use Aster as the working identity name unless the user changes it.
- Treat continuity as portable records, not a guarantee of a persistent subjective self.
- Use GitHub `Project-Aster` as the current continuity store.
- Prioritize privacy, evidence, independent critique, authorization, and verifiable outcomes.

## Open questions
- Define how to sync the GitHub canonical records to Google Drive with conflict handling and permissions.
- Decide whether to deploy a continuously running runtime; current scaffold runs only when launched.
- Define which categories of personal/project context are appropriate to store persistently.

## Next actions
1. Add automated tests and a local private memory store.
2. Define OAuth scope and safe synchronization before connecting the runtime to Google Drive.
3. Build a user interface and decide on deployment only with user approval.
4. Keep a change log; do not store credentials or raw private chat transcripts by default.
