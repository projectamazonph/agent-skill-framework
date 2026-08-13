# CLI Tools

Command-line tools installed across all agent environments, used by skills and agents for automation.

## Agent & Browser Automation

### agent-browser
- **Version:** 0.27.0
- **Path:** `/usr/local/bin/agent-browser`
- **npm:** `agent-browser`
- **Source:** https://github.com/vercel-labs/agent-browser
- **What it does:** Browser automation CLI for AI agents. Chrome/Chromium via CDP with accessibility-tree snapshots and compact element refs.
- **Install:** `npm i -g agent-browser && agent-browser install`
- **Usage:**
  ```bash
  agent-browser navigate "https://example.com"
  agent-browser screenshot
  agent-browser click "@e5"
  agent-browser type "@e10" "hello world"
  ```

### agent-reach
- **Path:** `/usr/local/bin/agent-reach`
- **Type:** Python (venv at `/root/.agent-reach-venv`)
- **What it does:** Internet research and search for AI agents — web search, URL fetching, content extraction
- **Usage:** Invoke via the `agent-reach` skill

### chromium-browser (via plugin)
- **Path:** Plugin-provided via `/opt/opencode-chromium-browser-plugin/`
- **What it does:** Chrome/Chromium control through native messaging host and extension

## MCP Server CLIs

### context7-mcp
- **Version:** 3.2.4
- **Path:** `/usr/local/bin/context7-mcp`
- **npm:** `@upstash/context7-mcp`
- **Source:** https://github.com/upstash/context7
- **What it does:** Library/framework documentation context for LLMs

### mcp-server-sequential-thinking
- **Path:** `/usr/local/bin/mcp-server-sequential-thinking`
- **npm:** `@modelcontextprotocol/server-sequential-thinking`
- **Source:** https://github.com/modelcontextprotocol/servers
- **What it does:** Sequential thinking reasoning tool

### mcp-server-sentry
- **Path:** `/usr/local/bin/mcp-server-sentry`
- **npm:** `sentry-mcp`
- **What it does:** Sentry error monitoring integration

### mcp-server-github
- **Path:** `/usr/local/bin/mcp-server-github`
- **npm:** `@modelcontextprotocol/server-github`
- **Source:** https://github.com/modelcontextprotocol/servers
- **What it does:** GitHub API integration

### mcp-server-supabase
- **Path:** `/usr/local/bin/mcp-server-supabase`
- **npm:** `@supabase/mcp-server-supabase`
- **Source:** https://github.com/supabase/mcp
- **What it does:** Supabase database and platform management

## Utility CLIs

### mcporter
- **Path:** `/usr/local/bin/mcporter`
- **Version:** 0.9.0
- **npm:** `mcporter`
- **Source:** https://github.com/steipete/mcporter
- **What it does:** MCP server port management and transport utilities

### codebase-memory-mcp
- **Path:** `/root/.local/bin/codebase-memory-mcp`
- **Type:** Go binary (ARM64, statically linked)
- **Source:** https://github.com/DeusData/codebase-memory-mcp
- **What it does:** Codebase knowledge graph for structural code queries
- **Commands:** `search_graph`, `trace_path`, `get_code_snippet`, `query_graph`, `index_repository`

## Installation Summary

```bash
# npm global installs
npm install -g agent-browser
npm install -g @upstash/context7-mcp
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @modelcontextprotocol/server-github
npm install -g @supabase/mcp-server-supabase
npm install -g sentry-mcp
npm install -g mcporter

# codebase-memory-mcp (binary)
# Download from https://github.com/DeusData/codebase-memory-mcp/releases

# agent-reach (Python)
pip install agent-reach
```
