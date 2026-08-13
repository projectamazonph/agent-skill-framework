#!/usr/bin/env python3
"""Validate the Design Skill Pack structure and skill files.

Platform-agnostic — no tooling dependencies. Just checks file structure.
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

errors = []
warnings = []

def check(path, condition, msg):
    if not condition:
        errors.append(f"{path}: {msg}")

# 1. Skills directory
skills_dir = ROOT / 'skills'
check('skills/', skills_dir.is_dir(), "Missing skills/ directory")
if skills_dir.is_dir():
    md_files = sorted(skills_dir.glob('*.md'))
    check('skills/', len(md_files) > 0, "No .md files in skills/")
    for f in md_files:
        content = f.read_text()
        check(f.name, '---' in content, "Missing YAML frontmatter (starting ---)")
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2:
                fm = parts[1]
                check(f.name, 'name:' in fm, "Missing 'name:' in frontmatter")
                check(f.name, 'description:' in fm, "Missing 'description:' in frontmatter")
        # Check for required sections
        for section in ['Design Tokens', 'Anti-Patterns', 'Quality Gates']:
            if section not in content:
                warnings.append(f"{f.name}: Missing '{section}' section (recommended)")

# 2. Documentation
docs_dir = ROOT / 'docs'
check('docs/', docs_dir.is_dir(), "Missing docs/ directory")
if docs_dir.is_dir():
    for doc in ['ARCHITECTURE.md', 'CONTRIBUTING.md', 'SKILL-CATALOG.md']:
        check(f'docs/{doc}', (docs_dir / doc).exists(), f"Missing {doc}")

# 3. Required root files
for f in ['README.md', 'AGENTS.md', 'LICENSE']:
    check(f, (ROOT / f).exists(), f"Missing {f}")

# Summary
if errors:
    print(f"❌ {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

if warnings:
    print(f"⚠️  {len(warnings)} warning(s):")
    for w in warnings:
        print(f"  - {w}")

skill_count = len(list(skills_dir.glob('*.md'))) if skills_dir.is_dir() else 0
doc_count = len(list(docs_dir.glob('**/*.md'))) if docs_dir.is_dir() else 0
print(f"✅ All checks passed — {skill_count} skill files, {doc_count} documentation files")
sys.exit(0)
