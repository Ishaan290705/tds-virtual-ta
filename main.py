from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Request model
class QARequest(BaseModel):
    question: str
    image: Optional[str] = None

# Link format
class Link(BaseModel):
    url: str
    text: str

# Response model
class QAResponse(BaseModel):
    answer: str
    links: List[Link]

# Root route
@app.get("/")
def root():
    return {
        "message": "TDS Virtual TA is running. Use POST /api/ with your question."
    }

# Main API route
@app.post("/api/", response_model=QAResponse)
async def answer_question(data: QARequest):
    # Stubbed response
    return {
        "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
            }
        ]
    }

