from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from search import load_course_content, search_content

app = FastAPI()
docs = load_course_content()  # Load course docs once

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
