---
name: artifact-production
description: Create, update, format, render, verify, version, and organize professional artifacts including DOCX documents, PDFs, presentations, spreadsheets, dashboards, SOPs, briefs, scripts, reports, templates, and repository records. Use when work must become a polished downloadable file or reusable asset with explicit layout, typography, color, accessibility, metadata, versioning, naming, and QA standards. Preserve existing content and formatting during revisions unless change is requested.
---

# Artifact Production

## Mission

Turn approved content into a complete, polished, reusable artifact. Own presentation quality, file-format correctness, metadata, versioning, rendering, and final QA.

Do not change meaning to improve layout. Return unclear or incomplete source requirements to `conversation-compiler`.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. Mark `pass` only after the requested artifact is complete, rendered or opened, visually inspected, and functionally checked.

## Establish the Artifact Contract

Define:

- Purpose and audience
- Source-of-truth content
- Required format and delivery channel
- Brand or visual system
- Page, slide, sheet, viewport, duration, or file constraints
- Accessibility requirements
- Required metadata, status, and version
- Acceptance and rendering checks

Use the applicable file skill for DOCX, PDF, presentations, spreadsheets, charts, or interactive visualizations.

## Select the Standard

Read only the relevant references:

- [references/artifact-standards.md](references/artifact-standards.md) for format-specific structures
- [references/design-guidelines.md](references/design-guidelines.md) for visual and accessibility rules
- [references/metadata-and-versioning.md](references/metadata-and-versioning.md) for identity, naming, status, and folders
- [references/qa-checklists.md](references/qa-checklists.md) before delivery

## Build the Artifact

1. Preserve the approved content hierarchy.
2. Create the source artifact in the requested editable format.
3. Apply consistent styles, spacing, tables, charts, callouts, and navigation.
4. Use real content. Do not ship placeholders, lorem ipsum, empty tables, fake citations, or decorative charts without data.
5. Add metadata and version identity.
6. Export required derivative formats from the source artifact.
7. Render or open the output and inspect every page, slide, sheet, or responsive state.
8. Correct clipping, overflow, broken formulas, weak contrast, unreadable density, and inconsistent styles.
9. Re-run functional and visual checks after correction.

## Preserve Revisions

When updating an existing artifact:

- Retain all unrelated content.
- Retain formatting unless the requested change requires a local adjustment.
- Preserve file identity and version history.
- Change only the requested sections, cells, slides, or components.
- Record the reason and scope of the version.

Never replace a substantial artifact with a shorter rewrite merely because one section changed.

## Verify Delivery

Confirm:

- The file opens in its target format.
- Content is complete and accurate.
- Layout survives rendering.
- Navigation, formulas, charts, links, and controls work.
- Accessibility basics pass.
- Filename, status, version, and metadata match.
- No temporary, hidden, or duplicate output is presented as final.

Lead with the completed artifact and only the delivery details the user needs.
