"""Context Gateway: federated retrieval across pgvector, Graph Kernel, and Gemini embeddings.

A standalone FastAPI service that provides token-optimized context for Claude Code sessions
with echo suppression, duplicate detection, and overlap classification.
"""

__version__ = "1.0.0"
__version_info__ = tuple(int(x) for x in __version__.split("."))
