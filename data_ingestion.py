from document_processing import convert_and_preprocess_documents
from document_storage import setup_document_store
from embedding_retrieval import setup_embedding_retriever

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main":
    pdf_paths = ["data/cds_survey_final.pdf"]
    host = 'http://localhost'
    port = 8080
    embedding_dim = 384
    index_name = "CDS"
    embedding_model = "sentence-transformers/all-MiniLM-L6-v2"

    logger.info("Converting and preprocessing documents...")
    preprocessed_docs = convert_and_preprocess_documents(pdf_paths)

    logger.info("Setting up the document store...")
    document_store = setup_document_store(host, port, embedding_dim, index_name)

    logger.info("Writing preprocessed documents to the document store...")
    document_store.write_documents(preprocessed_docs)

    logger.info("Setting up the embedding retriever...")
    retriever = setup_embedding_retriever(document_store, embedding_model)

    logger.info("Updating document embeddings...")
    document_store.update_embeddings(retriever)
