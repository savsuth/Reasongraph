"""
Reasongraph MCP Server Package

A full Model Context Protocol (MCP) server for Reasongraph — exposes knowledge graph
construction, semantic extraction, decision intelligence, reasoning, analytics,
and export capabilities as MCP tools and resources.

Run the server:
    python -m mcp.server        # from repo root
    python -m reasongraph.mcp_server  # alias inside installed package

Configure in Claude Desktop, Windsurf, Cline, Continue, VS Code:
    {
        "mcpServers": {
            "reasongraph": {
                "command": "python",
                "args": ["-m", "mcp.server"],
                "cwd": "/path/to/reasongraph"
            }
        }
    }
"""

# `reasongraph.__version__` is the authoritative package version — see
# reasongraph/mcp_server/__init__.py for why it is used directly rather than
# importlib.metadata.version("reasongraph").
from reasongraph import __version__

from .server import ReasongraphMCPServer, main

__all__ = ["ReasongraphMCPServer", "main", "__version__"]
