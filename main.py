from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer_question(req: QuestionRequest):
    return {
        "answer": "This is a placeholder answer.",
        "links": [
            {"url": "https://example.com", "text": "Sample reference"}
        ]
    }
