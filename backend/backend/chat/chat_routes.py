from fastapi import APIRouter
from pydantic import BaseModel
from backend.chat.conversation_handler import ask_ai

router = APIRouter()

class ChatInput(BaseModel):
    query: str

@router.post("/chat/")
def chat(input: ChatInput):
    response = ask_ai(input.query)
    return {"response": response}
