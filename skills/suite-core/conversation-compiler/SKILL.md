---
name: conversation-compiler
description: Convert raw AI conversations, transcripts, research dumps, and mixed notes into governed projects, prioritized deliverable graphs, implementation tasks, and export-ready artifact specifications. Use when the source contains scattered ideas, corrections, commitments, unresolved questions, or requested files across coding, course creation, company documentation, operations, or other multi-deliverable work. Preserve source traceability and route final file production through artifact-production.
---

# Conversation Compiler

## Mission

Turn conversation debt into execution assets. Extract what was actually requested, preserve corrections and constraints, expose missing decisions, and produce the smallest complete deliverable set in dependency order.

Do not invent requirements to make a package look complete.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. Mark `pass` only when every approved requirement and deliverable has source evidence, dependency order, and acceptance criteria.

## Ingest the Source

1. Preserve source order, speakers, dates, attachments, and referenced artifacts when available.
2. Separate user requirements from assistant proposals.
3. Treat later explicit corrections as superseding earlier statements while retaining the decision history.
4. Mark uncertain statements, rejected options, unresolved questions, and implicit dependencies.
5. Deduplicate repeated ideas without erasing stronger later detail.

## Build the Evidence Ledger

Extract:

- Desired outcomes
- Audiences and users
- Functional requirements
- Non-functional requirements
- Constraints and exclusions
- Decisions and corrections
- Deliverables explicitly requested
- Deliverables implied by execution dependencies
- Existing assets and source files
- Open questions and blockers
- Risks, urgency, sentiment, and confidence

Attach a source pointer or concise quote to every material requirement. Never promote an assistant suggestion to a binding requirement without user evidence.

## Classify the Project

Use one or more packs:

| Pack | Common outputs |
| --- | --- |
| Coding project | PRD, MVP scope, architecture, data model, API spec, task plan, tests, agent prompts, deployment plan |
| Course creation | curriculum map, modules, lesson plans, teaching scripts, handouts, worksheets, assessments, slides |
| Company documentation | SOPs, policies, RACI, decision trees, templates, trackers, reports, onboarding packs |
| Amazon PPC operations | audit, decision matrix, campaign plan, SOPs, trackers, reporting deck, training drills |
| General execution | proposal, roadmap, task list, briefing pack, decision log, artifact set |

Read [references/deliverable-packs.md](references/deliverable-packs.md) for dependency order and completeness rules.

## Create the Deliverable Graph

For each candidate deliverable, record:

```text
Name
Purpose
Audience
Source requirements
Dependencies
Output format
Template
Status: required | recommended | optional | blocked
Acceptance criteria
Owner or target skill
```

Prioritize:

1. Source-of-truth documents
2. Decisions and specifications required by downstream work
3. Execution assets
4. Training or communication assets
5. Presentation and export variants

Do not generate five decorative summaries while the source-of-truth specification is missing.

## Manage the Idea Debt Inbox

Place uncommitted but useful ideas into an Idea Debt Inbox with:

- Idea
- Source
- Expected value
- Required decision
- Dependency
- Effort and risk estimate
- Recommended action: now, later, reject, or investigate

Keep Idea Debt separate from approved scope.

## Decide Whether to Ask

Ask only when a missing answer would materially change behavior, architecture, audience, cost, or deliverable format. Otherwise proceed with a flagged, conservative assumption.

Never use placeholders in final assets. A blocked artifact remains in the graph as blocked rather than being generated with fake content.

## Compile the Execution Package

Produce:

1. Executive project brief
2. Requirements and corrections ledger
3. Deliverable graph
4. Dependency-ordered task plan
5. Idea Debt Inbox
6. Risks and missing decisions
7. Artifact specifications for `artifact-production`
8. Coding handoff for `engineering-orchestrator` when applicable
9. Trust ledger mapping each output to its sources and QA status

## Preserve Trust

- Maintain source traceability.
- Label inference separately from user-stated fact.
- Preserve rejected decisions so they are not resurrected later.
- Record template and version used for every generated asset.
- Record exports to DOCX, PDF, PPTX, XLSX, or other formats.
- Keep generated assets linked to their source conversation and project.

## Return the Handoff

Lead with the project and required deliverables. Provide dependency order, blocked decisions, and exact next skill. Do not generate polished files inside this skill when artifact-production or a format-specific skill should own them.
