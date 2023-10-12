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
        ├── document_query_processing.py
        ├── document_query_storage.py
        ├── embedding_retrieval.py
        ├── main.py
    ```

# Step 1: Install Dependencies

You can install the required Python dependencies by running:

```bash
pip install haystack sentence-transformers
```

# Step 2: Run the Ingestion Flow

### Convert PDF to Text
Our first step is to convert the PDF document to text. This is crucial for subsequent processes.

### Set Up Document Storage  
Next, we'll set up the Weaviate document store. This is where we store documents and their embeddings.

### Initialize the Retrieval Component 
In `retrieval.py`, we'll initialize the `EmbeddingRetriever`, which retrieves documents based on embeddings.

### Set Up the Model
In `model.py`, we'll set up the `PromptModel`, allowing us to answer questions based on the documents.

### Configure the Query Pipeline
We'll use `query.py` to configure the query pipeline, connecting the retriever and model. This pipeline handles retrieval and QA.

# Step 3: Run the Main Script
Now execute `main.py` which orchestrates the entire query flow:

- Receives question  
- Converts PDF to text
- Sets up Weaviate store
- Initializes `EmbeddingRetriever`
- Initializes `PromptModel` 
- Configures query pipeline
- Executes pipeline to answer question
- Logs the answer

Run with:

```bash
python main.py
```

# Step 4: Check the Answer 
After running, you'll get the answer and relevant docs.  

You've now set up the CDS query flow! 🎉 Ask questions and get detailed answers.

Happy querying!