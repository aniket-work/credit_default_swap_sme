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




# Query Flow Guide 🚀

This guide will take you through the step-by-step process of setting up the Credit Default Swap (CDS) Query Flow. 📈

## Prerequisites 📋

Before we get started, make sure you have the following prerequisites in place:

- A Python environment with the necessary dependencies (you can install them using `pip`).
- The original PDF document, `cds_survey_final.pdf`, that you want to query.
- Your project directory should be structured as follows: 📂

    ```markdown
        ├── data
        │   └── cds_survey_final.pdf
        ├── document_processing.py
        ├── document_storage.py
        ├── embedding_retrieval.py
        ├── main.py
    ```

Step 1: Install Dependencies 🛠️
You can install the required Python dependencies by running the following command:

    ```bash
    pip install haystack sentence-transformers
    ```

Step 2: Run the Ingestion Flow 🚀
Convert PDF to Text 📄: Our first step is to convert the PDF document to text. This is crucial for the subsequent processes.

Set Up Document Storage 🗂️: Next, we'll set up the Weaviate document store. This is where we store our documents and their embeddings.

Initialize the Retrieval Component 🔄: In the retrieval.py module, we'll initialize the EmbeddingRetriever, which retrieves documents based on their embeddings.

Set Up the Model 🤖: In the model.py module, we'll set up the PromptModel, allowing us to answer questions based on the provided documents.

Configure the Query Pipeline 📊: We'll use the query.py module to configure the query pipeline, connecting the retriever and the model. This pipeline handles document retrieval and question answering.

Step 3: Run the Main Script 📜
Now it's time to execute the main.py script, which orchestrates the entire query flow. It does the following:

Receives your question.
    - Converts the PDF document to text.
    - Sets up the Weaviate document store.
    - Initializes the EmbeddingRetriever.
    - Initializes the PromptModel.
    - Configures the query pipeline.
    - Executes the query pipeline for answering your question.
    - Logs the answer.
    - Use the following command to run the main script:

    ```bash
    python main.py
    ```

Step 4: Check the Answer ✔️
After running the script, you'll receive the answer to your question, along with the relevant documents that support the answer.

And that's it! You've successfully set up and executed the CDS query flow. 🎉 You can now ask questions and receive detailed answers based on the provided documents.


Happy querying! 🚀

