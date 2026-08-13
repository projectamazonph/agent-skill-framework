# Ponytail Plugin

**Version:** 4.8.4  
**Author:** Dietrich Gebert  
**License:** MIT  
**Source:** https://github.com/DietrichGebert/ponytail

## What It Does

Lazy senior dev mode. Forces the simplest, shortest solution that actually works: YAGNI, stdlib first, no unrequested abstractions.

## Installation

### Codex CLI
```bash
# Install from marketplace
codex marketplace install ponytail
```

### OpenCode
```bash
# Add to opencode.json
{
  "plugin": ["./.opencode/plugins/ponytail.mjs"]
}
```

### npm
```bash
npm install -g @dietrichgebert/ponytail
```

## Provided Skills
- `ponytail` — Main lazy-dev mode
- `ponytail-review` — Code review for over-engineering
- `ponytail-audit` — Whole-repo audit
- `ponytail-debt` — Harvest ponytail: comments into debt ledger
- `ponytail-gain` — Impact scoreboard
- `ponytail-help` — Quick reference

## Provided Commands
- `/ponytail` — Toggle lazy mode
- `/ponytail-review` — Review a diff
- `/ponytail-audit` — Audit entire repo
- `/ponytail-debt` — Show debt ledger
- `/ponytail-gain` — Show metrics
- `/ponytail-help` — Show help

## Hooks
- `pre_llm_call` — Injects lazy-dev context before LLM calls
- `pre_gateway_dispatch` — Modifies behavior at gateway level
