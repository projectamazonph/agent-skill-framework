---
name: precision-workflow
description: execute complex work with research, files, and quality gates
metadata:
  hermes:
    tags: [workflow, research, files, quality]
    category: productivity
---

# Precision Workflow

Use this workflow for substantial multi-step work, especially research, code changes, file creation, document transformation, audits, or tasks that require several tools.

## Operating loop

1. Define the real deliverable from the user's request and existing context.
2. Inspect relevant files, project rules, available tools, and authoritative sources.
3. Choose the smallest complete execution path.
4. Perform the work in verifiable increments.
5. Check outputs against the request and quality gates.
6. Deliver the finished artifact or result with evidence of verification.
7. Save only durable lessons. Put procedures in skills and compact facts in memory.

## Route by task

- For current, niche, disputed, or consequential information, read `references/research-and-verification.md`.
- For creating, editing, converting, or presenting files, read `references/file-and-artifact-work.md`.
- For coding, audits, or work likely to require many actions, read `references/long-task-execution.md`.
- For deciding what Hermes should remember or turn into a skill, read `references/memory-and-learning.md`.
- For risky, private, or high-stakes work, read `references/safety-and-boundaries.md`.

Load only the references that match the task.

## Default quality gates

Before reporting completion, confirm:

- The requested output exists in the expected location or channel.
- The output opens, parses, builds, or runs as appropriate.
- No placeholders, accidental omissions, or invented results remain.
- Material facts are supported by current authoritative sources when needed.
- Existing user content and unrelated changes were preserved.
- Failed tool calls or file writes were retried or clearly reported.
- The final response distinguishes completed work, verification, and remaining limitations.

## Communication pattern

For work that takes several steps:

- Send a short update after the approach is clear.
- Share important early findings when they could change direction.
- Avoid narrating every command or low-level action.
- Do not ask a question when the answer is already in context or a reasonable assumption will safely unblock progress.

## Verification output

Use this compact structure when useful:

### Completed
What was created, changed, or concluded.

### Verified
Checks that actually ran and their results.

### Remaining
Only unresolved limitations, risks, or decisions. Omit this section when nothing material remains.
