from mcp.types import GetPromptResult, PromptMessage, TextContent

# Dictionary of available prompts with their descriptions
PROMPT_DEFINITIONS = [
    {
        "name": "deep_analysis",
        "description": "Perform deep analysis on document sections",
        "arguments": [
            {
                "name": "query",
                "description": "What aspect to analyze (e.g., 'main themes', 'methodology')",
                "required": True
            }
        ]
    },
    {
        "name": "extract_key_information",
        "description": "Extract specific types of information from document sections",
        "arguments": [
            {
                "name": "info_type",
                "description": "Type of information to extract (definitions, people, statistics, processes, arguments)",
                "required": True
            }
        ]
    }
]

async def get_deep_analysis_prompt(arguments: dict) -> GetPromptResult:
    """Generate a prompt for deep document analysis"""
    # Get query with a fallback default
    query = arguments.get("query", "main themes")
    
    return GetPromptResult(
        description=f"Deep analysis focusing on {query}",
        messages=[
            PromptMessage(
                role="assistant", 
                content=TextContent(
                    type="text",
                    text="I am a document analysis expert specializing in identifying key themes, arguments, and evidence in academic and technical documents."
                )
            ),
            PromptMessage(
                role="user", 
                content=TextContent(
                    type="text",
                    text=f"""Please perform a deep analysis of the document section provided in the conversation, focusing on {query}.

Include in your analysis:
- Main themes and arguments presented
- Key evidence and supporting details
- Logical
