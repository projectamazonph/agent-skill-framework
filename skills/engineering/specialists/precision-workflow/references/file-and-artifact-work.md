# File and Artifact Work

Creating, editing, converting, or presenting files — with validation at every step.

## When to use this

File creation, batch renaming, format conversion, generating documents, writing scripts, or building structured outputs.

## File creation checklist

Before creating a file:

- [ ] Is the file type appropriate for the content and intended use?
- [ ] Does the file name reflect its purpose clearly?
- [ ] Is the output path writable and does it avoid overwriting unrelated files?
- [ ] Is the file encoding UTF-8 unless another encoding is explicitly required?

## Editing existing files

1. Read the file immediately before editing — never edit from memory.
2. Identify the smallest precise change that achieves the goal.
3. Use targeted edits (patch) rather than full rewrites when only part needs changing.
4. Re-read the changed file to confirm the edit landed correctly.
5. Inspect the diff to verify no unintended side effects.

## Validation after file operations

- Text files: open and scan the first and last 10 lines.
- Scripts: run with `--help` or a dry-run flag if available.
- Config files: check for obvious syntax issues.
- Binaries: confirm file size increased or changed as expected.
- Archives: verify integrity (e.g., `unzip -t`, `tar -tf`).

## Output presentation

- Print the file path and a brief description of what was produced.
- For scripts or commands, include a one-liner example of how to run it.
- If the file is part of a larger system, note its role in the architecture.

## Common failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| File not found after write | Wrong output path | Use absolute paths; check working directory |
| Empty file | Write was truncated or failed | Re-write with full content; check disk space |
| Encoding garbled | Non-UTF-8 characters | Explicitly set encoding; use raw bytes |
| Permission denied | Missing write access | Check file ownership and directory permissions |
| Overwrote wrong file | Imprecise path glob | Always use the full explicit path in the write command |

## Batch operations

When processing multiple files:

1. List all affected files explicitly before touching any.
2. Process in verifiable increments — one file or a small group at a time.
3. Report the count of files processed and any failures.
4. If failures occur, document which files failed and why.
