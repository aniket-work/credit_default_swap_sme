from haystack.nodes import EmbeddingRetriever

def setup_embedding_retriever(document_store, embedding_model):
    """
    Sets up the EmbeddingRetriever for document retrieval.

    Args:
        document_store (WeaviateDocumentStore): Document store for embeddings.
        embedding_model (str): Name of the embedding model.

    Returns:
        EmbeddingRetriever: Initialized EmbeddingRetriever.
    """
    retriever = EmbeddingRetriever(document_store=document_store, embedding_model=embedding_model)
    return retriever
