# MCP Servers

Model Context Protocol servers configured across all agent installations. These provide tools and context to AI agents.

## Installed MCP Servers

### codebase-memory-mcp
- **Binary:** `/root/.local/bin/codebase-memory-mcp`
- **Source:** https://github.com/DeusData/codebase-memory-mcp
- **Type:** Go binary (statically linked, ARM64)
- **What it does:** Maintains a knowledge graph of the codebase for structural code queries (search_graph, trace_path, get_code_snippet, query_graph)
- **Config (Codex):**
  ```toml
  [mcp_servers.codebase-memory-mcp]
  command = "/root/.local/bin/codebase-memory-mcp"
  ```
- **Config (OpenCode):**
  ```json
  {
    "mcp": {
      "codebase-memory-mcp": {
        "enabled": true,
        "type": "local",
        "command": ["/root/.local/bin/codebase-memory-mcp"]
      }
    }
  }
  ```

### context7
- **Binary:** `/usr/local/bin/context7-mcp`
- **npm:** `@upstash/context7-mcp`
- **Source:** https://github.com/upstash/context7
- **What it does:** Up-to-date documentation context for LLMs — fetches real docs for libraries and frameworks
- **Config:**
  ```toml
  [mcp_servers.context7]
  command = "context7-mcp"
  ```

### sequential-thinking
- **Binary:** `/usr/local/bin/mcp-server-sequential-thinking`
- **npm:** `@modelcontextprotocol/server-sequential-thinking`
- **Source:** https://github.com/modelcontextprotocol/servers
- **What it does:** Provides a sequential thinking tool for complex reasoning chains
- **Config:**
  ```toml
  [mcp_servers.sequential-thinking]
  command = "mcp-server-sequential-thinking"
  ```

### sentry
- **Binary:** `/usr/local/bin/mcp-server-sentry`
- **npm:** `sentry-mcp`
- **Source:** https://github.com/getsentry/sentry-mcp (approx.)
- **What it does:** Connects to Sentry for error monitoring, issue tracking, and diagnostics
- **Config:**
  ```toml
  [mcp_servers.sentry]
  command = "mcp-server-sentry"
  environment = { SENTRY_AUTH_TOKEN = "<token>", TRANSPORT = "stdio" }
  ```

### github
- **Binary:** `/usr/local/bin/mcp-server-github`
- **npm:** `@modelcontextprotocol/server-github`
- **Source:** https://github.com/modelcontextprotocol/servers
- **What it does:** GitHub API access — repos, issues, PRs, code search, actions
- **Config:**
  ```toml
  [mcp_servers.github]
  command = "mcp-server-github"
  ```

### supabase
- **Binary:** `/usr/local/bin/mcp-server-supabase`
- **npm:** `@supabase/mcp-server-supabase`
- **Source:** https://github.com/supabase/mcp
- **What it does:** Supabase database management, edge functions, auth, and storage
- **Config:**
  ```toml
  [mcp_servers.supabase]
  command = "mcp-server-supabase"
  ```

### figma
- **Type:** Remote HTTP
- **Source:** https://mcp.figma.com/mcp
- **What it does:** Figma design file access, node inspection, variable extraction, asset export
- **Config:**
  ```toml
  [mcp_servers.figma]
  url = "https://mcp.figma.com/mcp"
  bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
  http_headers = { "X-Figma-Region" = "us-east-1" }
  ```

## Config Files

| Config File | Location | Format |
|-------------|----------|--------|
| Codex global | `/root/.codex/config.toml` | TOML |
| OpenCode | `/root/.config/opencode/opencode.json` | JSON |

## Installation Commands

```bash
# npm-based MCP servers
npm install -g @upstash/context7-mcp
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @modelcontextprotocol/server-github
npm install -g @supabase/mcp-server-supabase
npm install -g sentry-mcp

# codebase-memory-mcp (binary release)
curl -fsSL https://github.com/DeusData/codebase-memory-mcp/releases/latest/download/codebase-memory-mcp-linux-arm64 -o /usr/local/bin/codebase-memory-mcp
chmod +x /usr/local/bin/codebase-memory-mcp
```
