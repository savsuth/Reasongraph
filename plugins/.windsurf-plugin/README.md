# Reasongraph — Windsurf Plugin

> **v0.4.0** — Adds all 17 Reasongraph skills, 3 agents, and hook configuration to Windsurf.

## MCP Server Setup (recommended)

Add to your Windsurf MCP config (`~/.codeium/windsurf/mcp_config.json`):

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

Windsurf will have access to all 17 Reasongraph skills (`extract`, `record_decision`, `query_decisions`, `find_precedents`, `get_causal_chain`, `add_entity`, `add_relationship`, `run_reasoning`, `get_graph_analytics`, `export_graph`, and more) directly in the AI panel.

## Skills

All 17 skills under `plugins/skills/` are available as slash commands once the plugin is loaded:

`extract` · `ingest` · `query` · `ontology` · `validate` · `deduplicate` · `embed` · `reason` · `decision` · `causal` · `temporal` · `provenance` · `policy` · `explain` · `export` · `change` · `visualize`

## Knowledge Explorer

```bash
reasongraph-explorer --graph my_graph.json --port 8000
```

Open `http://localhost:5174` for the interactive graph dashboard.

## Requirements

- Python 3.10+
- `pip install reasongraph`
