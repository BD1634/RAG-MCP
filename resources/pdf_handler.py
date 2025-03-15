import os
import glob
from mcp.types import Resource
from langchain_community.document_loaders import PyPDFLoader
from ..config import logger, PDF_DIRECTORY

def list_pdf_resources() -> list[Resource]:
    """List all available PDF resources"""
    resources = []

    try:
        pdf_files = glob.glob(f"{PDF_DIRECTORY}/*.pdf")
        for pdf_path in pdf_files:
            filename = os.path.basename(pdf_path)
            name_without_ext = os.path.splitext(filename)[0]
            
            resources.append(
                Resource(
                    uri=f"document://pdf/{name_without_ext}",
                    name=name_without_ext.replace('_', ' ').title(),
                    description=f"PDF Document: {name_without_ext}",
                    mimeType="application/pdf"
                )
            )
    except Exception as e:
        logger.error(f"Error scanning for PDF files: {e}")
    
    return resources

async def read_pdf_resource(uri: str) -> str:
    """Read content from a PDF resource"""
    path_parts = str(uri).split("/")
    if len(path_parts) < 4:
        raise ValueError(f"Invalid URI format: {uri}")
    
    document_name = path_parts[3]
    
    try:            
        # Construct path 
        path = f"{PDF_DIRECTORY}/{document_name}"
        if not path.endswith('.pdf'):
            path += '.pdf'
            
        # Load the document
        loader = PyPDFLoader(path)
        pages = loader.load()
        
        # Combine all pages into one text with page markers
        full_text = ""
        for i, page in enumerate(pages):
            full_text += f"\n\n--- Page {i+1} ---\n\n"
            full_text += page.page_content
        logger.info(f"Loaded document {document_name} with {len(pages)} pages. Preview: {full_text[:200]}...")
        return full_text
    except Exception as e:
        error_message = f"Error loading document: {str(e)}"
        logger.error(error_message)
        return error_message
