from haystack.nodes import EmbeddingRetriever

def setup_retriever(document_store):
    """
    Sets up the EmbeddingRetriever for document retrieval.

    Args:
        document_store (WeaviateDocumentStore): Document store for embeddings.

    Returns:
        EmbeddingRetriever: Initialized EmbeddingRetriever.
    """
    return EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/all-MiniLM-L6-v2"
    )
