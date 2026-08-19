# Reasongraph Plugins (Community Guide)

> **v0.4.0** — 17 domain skills · 3 agents · 8 platform plugins · Knowledge Explorer UI

Reasongraph ships a shared plugin bundle under `plugins/` that works across every major AI coding assistant. Connect any supported platform to Reasongraph's knowledge graph engine for semantic extraction, decision intelligence, reasoning, provenance, ontology, and export workflows.

---

## Platform Plugins

Reasongraph provides a dedicated plugin for each platform. Every plugin shares the same `skills/`, `agents/`, and `hooks/` bundle — only the manifest format differs.

| # | Platform | Plugin Folder | Setup |
|---|----------|--------------|-------|
| 1 | **Claude Code** | `.claude-plugin/` | `claude --plugin-dir ./plugins` |
| 2 | **Cursor** | `.cursor-plugin/` | Cursor Marketplace → refresh |
| 3 | **Codex** | `.codex-plugin/` | Marketplace UI → install |
| 4 | **Cline** | `.cline-plugin/` | Cline MCP settings |
| 5 | **Windsurf** | `.windsurf-plugin/` | `mcp_config.json` |
| 6 | **Continue** | `.continue-plugin/` | `~/.continue/config.json` |
| 7 | **OpenClaw** | `.openclaw-plugin/` | `mcporter.json` |
| 8 | **VS Code** | `.vscode-plugin/` | `settings.json` MCP entry |

---

## What's Included

```
plugins/
├── skills/              # 17 domain skills (slash commands)
├── agents/              # 3 specialized agents
├── hooks/               # hooks.json
├── .claude-plugin/      # Claude Code manifest + marketplace
├── .cursor-plugin/      # Cursor manifest + marketplace
├── .codex-plugin/       # Codex manifest + marketplace
├── .cline-plugin/       # Cline manifest + marketplace
├── .windsurf-plugin/    # Windsurf manifest + marketplace
├── .continue-plugin/    # Continue manifest + marketplace
├── .openclaw-plugin/    # OpenClaw manifest + marketplace
└── .vscode-plugin/      # VS Code manifest + marketplace
```

### Skills (17)

`extract` · `ingest` · `query` · `ontology` · `validate` · `deduplicate` · `embed` · `reason` · `decision` · `causal` · `temporal` · `provenance` · `policy` · `explain` · `export` · `change` · `visualize`

### Agents (3)

`decision-advisor` · `explainability` · `kg-assistant`

---

## Prerequisites

```bash
git clone https://github.com/savsuth/Reasongraph.git
cd reasongraph
pip install reasongraph        # Python 3.10+
```

---

## Knowledge Explorer (v0.4.0)

Launch the interactive graph dashboard:

```bash
reasongraph-explorer --graph my_graph.json --port 8000
```

Open **http://localhost:5174** to explore:

- **Graph** — interactive canvas with ForceAtlas2 layout, path highlight, community coloring
- **Decisions** — causal chains and outcome analysis
- **Reasoning** — run deductive / abductive rules
- **SPARQL** — Monaco editor for graph queries
- **Vocabulary** — ontology concept tree
- **Lineage** — provenance lineage diagram
- **Import / Export** — JSON, RDF, Parquet, GraphML

---

## Installation by Platform

### Claude Code

```bash
claude --plugin-dir ./plugins
```

Or inside a session:

```bash
/plugin marketplace add ./plugins
/plugin install reasongraph@reasongraph-local
```

Verify:

```
/reasongraph:decision list
/reasongraph:explain decision <decision_id>
```

---

### Cursor

Cursor reads `.cursor-plugin/plugin.json` and `.cursor-plugin/marketplace.json` automatically. Publish the `plugins/` directory and refresh in Cursor Marketplace to pick up updates.

Verify:

```
/reasongraph:visualize topology
/reasongraph:reason deductive "IF Person(x) THEN Mortal(x)"
```

---

### Codex

1. Ensure your repo marketplace exists at `.agents/plugins/marketplace.json`.
2. Set `source.path` to `./plugins` in the plugin entry.
3. Restart Codex and install from the marketplace UI.

Verify:

```
/reasongraph:causal chain --subject <decision_id> --depth 3
```

---

### Cline

In Cline MCP settings, add:

```json
{
  "reasongraph": {
    "command": "python",
    "args": ["-m", "reasongraph.mcp_server"],
    "env": {}
  }
}
```

---

### Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "reasongraph": {
      "command": "python",
      "args": ["-m", "reasongraph.mcp_server"]
    }
  }
}
```

---

### Continue

Add to `~/.continue/config.json`:

```json
{
  "mcpServers": [
    {
      "name": "reasongraph",
      "command": "python",
      "args": ["-m", "reasongraph.mcp_server"]
    }
  ]
}
```

All 17 Reasongraph skills appear in the `@reasongraph` context provider dropdown.

---

### OpenClaw

Add to `~/.openclaw/mcporter.json`:

```json
{
  "mcpServers": {
    "reasongraph": {
      "command": "python",
      "args": ["-m", "reasongraph.mcp_server"],
      "transport": "stdio"
    }
  }
}
```

Then restart the gateway:

```bash
openclaw gateway restart
```

---

### VS Code

Add to `settings.json` (GitHub Copilot Chat):

```json
{
  "github.copilot.chat.mcp.servers": {
    "reasongraph": {
      "command": "python",
      "args": ["-m", "reasongraph.mcp_server"]
    }
  }
}
```

Or for the VS Code MCP extension:

```json
{
  "mcp.servers": {
    "reasongraph": {
      "command": "python",
      "args": ["-m", "reasongraph.mcp_server"]
    }
  }
}
```

---

## First Commands to Try

After installing on any platform:

```
/reasongraph:decision record <category> "<scenario>" "<reasoning>" <outcome> <confidence>
/reasongraph:decision list
/reasongraph:causal chain --subject <decision_id> --depth 3
/reasongraph:explain decision <decision_id>
/reasongraph:validate graph
/reasongraph:visualize topology
```

---

## Community Notes

- Keep `name` / `version` / `keywords` updated in each manifest before publishing.
- Keep skill frontmatter (`name` + `description`) consistent for reliable discovery.
- Include `plugins/` as-is when sharing — skills, agents, and hooks must stay bundled.
