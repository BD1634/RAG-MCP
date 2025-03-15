import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from ..config import logger, API_KEY, CHROMA_DB_PATH, COLLECTION_NAME, EMBEDDING_MODEL

class ChromaDBClient:
    """ChromaDB client wrapper for vector database operations"""
    
    def __init__(self):
        self.client = None
        self.embedding_function = None
        self.collection = None
        
    def initialize(self):
        """Initialize ChromaDB client, embedding function and collection"""
        try:
            # Connect to ChromaDB
            self.client = chromadb.PersistentClient(CHROMA_DB_PATH)
            logger.info("Successfully connected to ChromaDB")
            
            # Initialize embedding function if API key is available
            if API_KEY:
                self.embedding_function = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
                logger.info("Successfully initialized Embedding Function")
                
                # Get or create collection
                try:
                    self.collection = self.client.get_collection(
                        name=COLLECTION_NAME,
                        embedding_function=self.embedding_function
                    )
                    logger.info(f"Successfully connected to collection with {self.collection.count()} documents")
                except Exception:
                    self.collection = self.client.create_collection(
                        name=COLLECTION_NAME,
                        embedding_function=self.embedding_function
                    )
                    logger.info(f"Created new collection: {COLLECTION_NAME}")
            else:
                logger.warning("API key is not set - embedding function not initialized")
                
            return True
        except Exception as e:
            logger.error(f"Error initializing ChromaDB components: {e}")
            return False
    
    def query_collection(self, query_text, num_results=5):
        """Query the collection with the given text"""
        if not self.collection:
            raise ValueError("ChromaDB collection is not initialized")
            
        return self.collection.query(
            query_texts=[query_text],
            n_results=num_results
        )
    
    def get_collection_info(self):
        """Get information about the current collection"""
        if not self.collection:
            raise ValueError("ChromaDB collection is not initialized")
            
        return {
            "name": COLLECTION_NAME,
            "count": self.collection.count()
        }

# Create a singleton instance
db_client = ChromaDBClient()
