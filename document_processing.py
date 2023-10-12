from haystack.nodes import MarkdownConverter, PreProcessor
from haystack.preview.components.file_converters.pypdf import PyPDFToDocument

def convert_and_preprocess_documents(pdf_paths):
    """
    Converts PDF documents to text and preprocesses them.

    Args:
        pdf_paths (list): List of paths to PDF documents.

    Returns:
        list: Preprocessed documents.
    """
    converter = PyPDFToDocument()
    output = converter.run(paths=pdf_paths)
    documents = output["documents"]

    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=False,
        clean_header_footer=True,
        split_by="word",
        split_length=500,
        split_respect_sentence_boundary=True,
    )

    preprocessed_docs = []

    for doc in documents:
        new_doc = {
            'content': doc.text,
            'meta': doc.metadata,
        }
        preprocessed_docs.append(new_doc)

    return preprocessor.process(preprocessed_docs)
