from haystack.preview.components.file_converters.pypdf import PyPDFToDocument

def convert_to_text(pdf_paths):
    """
    Converts PDF documents to text.

    Args:
        pdf_paths (list): List of paths to PDF documents.

    Returns:
        list: List of text content from the PDFs.
    """
    converter = PyPDFToDocument()
    output = converter.run(paths=pdf_paths)
    return [doc.text for doc in output["documents"]]
