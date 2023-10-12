from haystack import Pipeline
from haystack.nodes import PromptNode, AnswerParser

def setup_query_pipeline(retriever, model, documents):
    """
    Sets up the query pipeline for document retrieval and answering questions.

    Args:
        retriever (EmbeddingRetriever): Document retriever component.
        model (PromptModel): PromptModel for question answering.
        documents (list): List of document content.

    Returns:
        Pipeline: Initialized query pipeline.
    """
    query_pipeline = Pipeline()
    query_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
    prompt_template = PromptTemplate(
        prompt=f"""Given the provided Documents, answer the Query. Make your answer detailed and long\n
                    Query: {{query}}\n
                    Documents: {{join(documents)}}
                    Answer: 
                """,
        output_parser=AnswerParser()
    )
    prompt_node = PromptNode(model_name_or_path=model, max_length=1000, default_prompt_template=prompt_template)
    query_pipeline.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
    return query_pipeline
