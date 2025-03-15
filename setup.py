from setuptools import setup, find_packages

setup(
    name="rag-mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mcp-server",
        "chromadb",
        "langchain-community",
        "python-dotenv",
        "sentence-transformers",
        "PyPDF2",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="RAG MCP Server for document search and analysis",
    keywords="rag, mcp, document, search",
    python_requires=">=3.9",
)
