from haystack.document_stores import WeaviateDocumentStore

def setup_document_store(host, port, index_name, embedding_dim):
    """
    Sets up the Weaviate document store for storing documents.

    Args:
        host (str): Weaviate server host.
        port (int): Weaviate server port.
        index_name (str): Name of the document index.
        embedding_dim (int): Dimension for document embeddings.

    Returns:
        WeaviateDocumentStore: Initialized Weaviate document store.
    """
    return WeaviateDocumentStore(
        host=host,
        port=port,
        index=index_name,
        embedding_dim=embedding_dim
    )
