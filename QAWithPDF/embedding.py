# from llama_index.core import VectorStoreIndex
# from llama_index.core import ServiceContext
# from llama_index.core import StorageContext, load_index_from_storage
# from llama_index.embeddings.gemini import GeminiEmbedding

# from QAWithPDF.data_ingestion import load_data
# from QAWithPDF.model_api import load_model

# import sys
# from exception import customexception
# from logger import logging

# def download_gemini_embedding(model,document):
#     """
#     Downloads and initializes a Gemini Embedding model for vector embeddings.

#     Returns:
#     - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
#     """
#     try:
#         logging.info("")
#         gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
#         service_context = ServiceContext.from_defaults(llm=model,embed_model=gemini_embed_model, chunk_size=800, chunk_overlap=20)
        
#         logging.info("")
#         index = VectorStoreIndex.from_documents(document,service_context=service_context)
#         index.storage_context.persist()
        
#         logging.info("")
#         query_engine = index.as_query_engine()
#         return query_engine
#     except Exception as e:
#         raise customexception(e,sys)
    




from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.settings import Settings  # Use Settings instead of ServiceContext

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("Initializing Gemini Embedding model")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        
        # Use Settings instead of ServiceContext
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        
        logging.info("Creating VectorStoreIndex")
        index = VectorStoreIndex.from_documents(document)
        
        logging.info("Persisting Storage Context")
        index.storage_context.persist()

        logging.info("Setting up query engine")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e, sys)
