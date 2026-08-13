# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-13

### Summary

Combined 5 GitHub skill repositories and 5 personal own skills into one comprehensive Agent Skill Framework.

### Added - Full Source Repository Integration

- **agent-skills-library** (projectamazonph/agent-skills-library): 46 skills (6 agent-skills + 40 mattpocock-skills)
- **agent-skill-suite** (projectamazonph/agent-skill-suite): 11 suite-core skills
- **engineering-standards** (projectamazonph/engineering-standards): 6 engineering skills + 1 specialist
- **design-skill-pack** (projectamazonph/design-skill-pack): 2 design skills
- **project-bootstrap-full** (projectamazonph/project-bootstrap-full): 1 bootstrap skill
- **Personal own skills**: 5 from skills-lock.json (critical-thinking, receiving-code-review, requesting-code-review, systematic-debugging, tdd-addyosmani)

### Added - Documentation

- New comprehensive README.md with quick reference, skill guide, and quick start
- Complete bundle.yaml with install_order, skill definitions, categories, sources, and responsibilities
- skill_aliases section documenting the 2 name collision resolutions
- SOURCE-REPOS.md mapping every skill to its source repository
- Updated CI workflow for multi-skill structure

### Added - Structure

- 7 unified skill categories: agent-skills, mattpocock-skills, suite-core, engineering, design, bootstrap, own
- integrations/ for Claude/Cursor/OpenAI platform configs
- adapters/ for claude-code, gemini-cli, github-copilot
- plugins/ for ponytail and chromium-browser
- schemas/, scripts/, docs/, references/ preserved from sources

### Fixed

- **Duplicate name "tdd"**: Deleted mattpocock-skills/engineering/tdd (identical to agent-skills/tdd)
- **Name collision "loop-engineering"**: Renamed engineering version to loop-engineering-v2 (different routing from suite-core version)
- **Name collision "test-driven-development"**: Renamed own version to tdd-addyosmani (different content from suite-core version)
- **Missing suite-core skills**: All 11 skills from agent-skill-suite now present (initial copy missed this directory)
- **CI workflow**: Updated to reference skills/bootstrap/SKILL.md instead of root SKILL.md

### Statistics

- 71 SKILL.md files (71 unique names, 0 duplicates)
- 317 total tracked files
- 7 skill categories
- 5 source GitHub repositories
- 5 personal own skills

### Validation Results

- 100% frontmatter valid (name + description in every SKILL.md)
- 95.5% have substantial body content (5+ lines)
- 3 thin skills are intentional (slash-command redirects with disable-model-invocation: true)
- 0 duplicate skill names after conflict resolution
