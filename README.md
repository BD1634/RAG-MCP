# RAG-MCP: Retrieval Augmented Generation with Model Control Protocol

A modular implementation of a Retrieval Augmented Generation server using the Model Control Protocol (MCP).

## Features

- Vector database integration with ChromaDB
- PDF document loading and processing
- Semantic search over document contents
- Specialized prompts for document analysis
- MCP server implementation with tools, resources, and prompts

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rag-mcp.git
cd rag-mcp
```

2. Install the package:
```bash
pip install -e .
```

3. Create a `.env` file based on the example:
```bash
cp .env.example .env
```

4. Edit the `.env` file with your API key and other settings:
```
API_KEY=your_api_key_here
CHROMA_DB_PATH=./chromadb
PDF_DIRECTORY=./testing
```

## Usage

### Running the Server

```bash
python -m rag_mcp.server
```

### Directory Structure

- `rag_mcp/`: Main package
  - `database/`: ChromaDB client and vector database operations
  - `tools/`: MCP tools implementation
  - `resources/`: Document resource handlers
  - `prompts/`: Specialized prompts for document analysis
- `tests/`: Unit tests

## Development

### Running Tests

```bash
python -m unittest discover
```

### Adding New Tools

1. Create a new file in the `tools` directory
2. Implement your tool function
3. Update the `TOOL_HANDLERS` and `TOOL_DEFINITIONS` in `tools/__init__.py`

### Adding New Prompts

1. Add your prompt implementation in `prompts/analysis_prompts.py`
2. Update the `PROMPT_HANDLERS` and `PROMPT_DEFINITIONS`

## License

MIT
