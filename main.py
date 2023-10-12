from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
import json
import re

from document_query_processing import convert_to_text
from document_query_storage import setup_document_store
from retrieval import setup_retriever
from model import initialize_model
from query import setup_query_pipeline

import logging
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def initialize_logging():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_answer")
async def get_answer(request: Request, question: str = Form(...)):
    logger = initialize_logging()
    logger.info(f"Received question: {question}")

    pdf_paths = ["data/cds_survey_final.pdf"]
    text_contents = convert_to_text(pdf_paths)
    document_store = setup_document_store(
        host='http://localhost',
        port=8080,
        index='CDS',
        embedding_dim=384
    )

    retriever = setup_retriever(document_store)
    model = initialize_model()
    query_pipeline = setup_query_pipeline(retriever, model, text_contents)

    json_response = query_pipeline.run(query=question, params={"Retriever": {"top_k": 3}})
    answers = json_response['answers'][0]
    answer = answers.answer

    documents = json_response['documents']
    document_info = "\n".join(doc.content for doc in documents)

    sentences = re.split(r'(?<=[.!?])\s', answer)
    complete_sentences = [sentence for sentence in sentences if re.search(r'[.!?]$', sentence)]
    updated_answer = ' '.join(complete_sentences)

    logger.info(f"Answer: {updated_answer}")

    response_data = jsonable_encoder({"answer": updated_answer, "relevant_documents": document_info})
    return JSONResponse(content=response_data)
