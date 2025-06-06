from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from search import load_course_content, search_content
import os

app = FastAPI()

# ✅ FIX: Use correct path for 'tds-content.xml'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
XML_PATH = os.path.join(BASE_DIR, "tds-content.xml")
docs = load_course_content(XML_PATH)  # Pass the correct path to loader

class QARequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class QAResponse(BaseModel):
    answer: str
    links: List[Link]

@app.get("/")
def root():
    return {"message": "TDS Virtual TA is running. Use POST /api/ with your question."}

@app.post("/api/", response_model=QAResponse)
async def answer_question(data: QARequest):
    answer, links = search_content(data.question, docs)
    return {"answer": answer, "links": links}

