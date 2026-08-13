# Metadata and Versioning

## Required Metadata

- Title
- Description or purpose
- Owner
- Source project or conversation
- Created and updated dates
- Status
- Version
- Format
- Tags
- Sensitivity
- Review or expiry date when applicable

## Status

Use: draft, in-review, approved, published, deprecated, or archived.

## Versioning

- Patch: correction that does not change meaning
- Minor: new compatible content or capability
- Major: structural, contractual, or audience-breaking change

Record the change reason and affected sections. Preserve stable file identity when updating the same artifact.

## Naming

Use descriptive, filesystem-safe names:

```text
project_artifact_audience_status_v1.2_2026-07-16.ext
```

Avoid names such as `final-final`, `new`, `latest2`, or unexplained abbreviations.

## Folder Pattern

```text
project/
  sources/
  working/
  approved/
  exports/
  archive/
```

Do not duplicate the canonical artifact across folders. Exports point back to the source version.

## Sensitivity

Use public, internal, confidential, or restricted. Do not embed secrets or private credentials in artifact metadata.
