from fastapi import APIRouter
from pydantic import BaseModel

from backend.graph.workflow import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.message
        }
    )

    return {
        "answer": result["answer"]
    }