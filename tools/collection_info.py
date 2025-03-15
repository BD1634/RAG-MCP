from mcp.types import TextContent
from ..database import db_client
from ..config import logger

async def get_collection_info(arguments: dict) -> list[TextContent]:
    """Get information about the ChromaDB collection"""
    try:
        if not db_client.collection:
            return [TextContent(
                type="text",
                text="Error: ChromaDB collection is not initialized. Please ensure the database is properly set up."
            )]
            
        info = db_client.get_collection_info()
        return [TextContent(
            type="text",
            text=f"Collection name: {info['name']}\nNumber of documents: {info['count']}"
        )]
    except Exception as e:
        error_message = f"Error getting collection info: {str(e)}"
        logger.error(error_message)
        return [TextContent(type="text", text=error_message)]
