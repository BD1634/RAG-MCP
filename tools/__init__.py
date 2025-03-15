from .document_query import query_document
from .collection_info import get_collection_info

# Dictionary mapping tool names to their handler functions
TOOL_HANDLERS = {
    "query_document": query_document,
    "get_collection_info": get_collection_info
}

# Tool definitions for MCP server
TOOL_DEFINITIONS = [
    {
        "name": "query_document",
        "description": "Search for information in the document based on semantic similarity",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query_text": {
                    "type": "string",
                    "description": "The search query text"
                },
                "num_results": {
                    "type": "integer",
                    "description": "Number of results to return (default: 5)"
                }
            },
            "required": ["query_text"]
        }
    },
    {
        "name": "get_collection_info",
        "description": "Get information about the ChromaDB collection",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]

__all__ = ['TOOL_HANDLERS', 'TOOL_DEFINITIONS']
