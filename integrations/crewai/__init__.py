"""
Reasongraph × CrewAI Integration
==============================

First-class integration between the Reasongraph semantic intelligence stack and
the `CrewAI <https://github.com/crewAIInc/crewAI>`_ agentic framework.

Public surface
--------------
ReasongraphKGTool         — CrewAI ``BaseTool`` exposing KG construction/query actions
ReasongraphDecisionTool   — CrewAI ``BaseTool`` exposing decision-intelligence actions
ReasongraphKnowledgeSource— CrewAI ``BaseKnowledgeSource`` giving crews graph knowledge

Quick start
-----------
    pip install reasongraph[crewai]

    >>> from integrations.crewai import (
    ...     ReasongraphKGTool,
    ...     ReasongraphDecisionTool,
    ...     ReasongraphKnowledgeSource,
    ... )

Compatibility
-------------
Requires ``crewai >= 0.80.0``.  All three classes degrade gracefully when
``crewai`` is not installed — they are still importable and carry the full
Reasongraph API, but cannot be passed to ``Crew`` / ``Agent`` constructors.
"""

from ._availability import CREWAI_AVAILABLE, CREWAI_IMPORT_ERROR
from .decision_tool import ReasongraphDecisionTool
from .kg_tool import ReasongraphKGTool
from .knowledge_source import ReasongraphKnowledgeSource

__all__ = [
    "ReasongraphKGTool",
    "ReasongraphDecisionTool",
    "ReasongraphKnowledgeSource",
    "CREWAI_AVAILABLE",
    "CREWAI_IMPORT_ERROR",
]

__version__ = "0.1.0"
