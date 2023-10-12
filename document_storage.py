from haystack.document_stores import WeaviateDocumentStore

def setup_document_store(host, port, embedding_dim, index_name):
    """
    Sets up the WeaviateDocumentStore for document storage.

    Args:
        host (str): Weaviate server host.
        port (int): Weaviate server port.
        embedding_dim (int): Dimension for document embeddings.
        index_name (str): Name of the document index.

    Returns:
        WeaviateDocumentStore: Initialized WeaviateDocumentStore.
    """
    document_store = WeaviateDocumentStore(host=host, port=port, embedding_dim=embedding_dim, index=index_name)
    return document_store
