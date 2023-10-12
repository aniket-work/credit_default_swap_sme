# Ingestion Flow
📂 ➡️ 📈

Here's a step-by-step guide for the data ingestion flow, where we prepare your environment and execute the script for processing Credit Default Swap (CDS) documents:

1. **Install Dependencies** 🔧
   - Make sure you have all the required dependencies installed, such as `haystack` and `sentence-transformers`. You can install them using pip:
     ```bash
     pip install haystack sentence-transformers
     ```

2. **Prepare Your Data** 📁
   - Ensure that the original PDF file, `cds_survey_final.pdf`, is in the `data` directory (or specify the correct path if it's located elsewhere).

3. **Organize Your Project Directory** 📂
   - Organize your project directory to keep things tidy:
     ```markdown
     ├── data
     │   └── cds_survey_final.pdf
     ├── document_processing.py
     ├── document_storage.py
     ├── embedding_retrieval.py
     ├── main.py
     ```

4. **Run the Ingestion Script** 🚀
   - Execute the `main.py` script to perform data ingestion and embedding retrieval:
     ```bash
     python main.py
     ```

   This script will handle the heavy lifting. It converts and preprocesses the PDF documents, sets up the Weaviate document store, writes the preprocessed documents to it, sets up the EmbeddingRetriever, and updates document embeddings.

5. **Check Weaviate Server** 💻
   - Ensure that the Weaviate server is running and accessible at the specified host and port (http://localhost:8080) for the document store to work correctly.

That's it! You're ready to unleash the power of Credit Default Swap data ingestion and retrieval. 💥
