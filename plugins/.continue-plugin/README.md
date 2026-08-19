# Reasongraph — Continue Plugin

> **v0.4.0** — Adds Reasongraph as an MCP server and context provider to [Continue.dev](https://continue.dev).

## MCP Server Setup

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

Continue will show all 17 Reasongraph skills in the `@reasongraph` context provider dropdown.

## Knowledge Explorer

```bash
reasongraph-explorer --graph my_graph.json --port 8000
```

Open `http://localhost:5174` for the interactive graph dashboard.

## Requirements

- Python 3.10+
- `pip install reasongraph`
