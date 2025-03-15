import os
import logging
import dotenv

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RAG-MCP")

# Load environment variables
dotenv.load_dotenv()

# Configuration constants
API_KEY = os.getenv("API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chromadb")
PDF_DIRECTORY = os.getenv("PDF_DIRECTORY", "./testing")
COLLECTION_NAME = "pdf_collection"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
