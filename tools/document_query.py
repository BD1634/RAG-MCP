from mcp.types import TextContent
from ..database import db_client
from ..config import logger

def format_search_result(document: str, distance: float, metadata: dict = None) -> str:
    """Format a search result into a readable string"""
    result = f'Score: {1 - distance:.4f} (closer to 1 is better)\n'

    if metadata:
        page_num = metadata.get("page", "Unknown")
        result += f"Page: {page_num}\n"
    
    result += f"Content: {document}"
    return result

async def query_document(arguments: dict) -> list[TextContent]:
    """Search for information in the document based on semantic similarity"""
    query_text = arguments.get("query_text", "")
    num_results = arguments.get("num_results", 5)

    try:
        if not db_client.collection:
            return [TextContent(
                type="text",
                text="Error: ChromaDB collection is not initialized. Please ensure the database is properly set up."
            )]
        
        results = db_client.query_collection(query_text, num_results)
        
        # Process results
        if not results or 'documents' not in results or not results['documents'][0]:
            return [TextContent(type="text", text="No results found for your query.")]
        
        formatted_results = []
        for i, (doc, distance, metadata) in enumerate(zip(
            results['documents'][0], 
            results['distances'][0],
            results['metadatas'][0] if 'metadatas' in results else [{}] * len(results['documents'][0])
        )):
            formatted_results.append(f"Result {i+1}:\n{format_search_result(doc, distance, metadata)}")
        
        return [TextContent(
            type="text",
            text="\n\n---\n\n".join(formatted_results)
        )]
    
    except Exception as e:
        error_message = f"Error querying document: {str(e)}"
        logger.error(error_message)
        return [TextContent(type="text", text=error_message)]
