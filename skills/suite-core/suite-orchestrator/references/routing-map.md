# Routing Map

## Combined Routes

| Request | Route |
| --- | --- |
| “Build this app from our conversation” | Conversation Compiler → Agent OS → Engineering Standards → Council checkpoint → Artifact Production → Memory |
| “Continue the repo” | Agent OS → Engineering Standards → Memory |
| “Audit this codebase” | Agent OS read-only state → Implementation Council → Engineering Quality Gates |
| “Turn this chat into a PRD and deck” | Conversation Compiler → Artifact Production |
| “Fix the bug” | Agent OS → Engineering Standards → Memory for reusable root cause |
| “Create a course from these notes” | Conversation Compiler → Artifact Production → Memory for durable curriculum decisions |
| “Set up local memory” | Agent Control Plane permission/state check → Local Memory |

## Handoff Contract

Pass only:

- Authorized scope
- Stable requirements and constraints
- Source evidence
- Decisions already made
- Exact blocker or next responsibility
- Required completion evidence

Do not pass speculation as a requirement or flood the next skill with irrelevant transcripts.

## Completion Owners

- Code and software changes: Engineering Quality Gates through the Engineering Standards Orchestrator
- Artifact files: Artifact Production QA and the applicable file-format skill's render verification
- Expert assessment: Implementation Council readiness verdict
- Memory operations: Local Memory readback or status evidence
- Agent control changes: Agent Control Plane state and permission audit
