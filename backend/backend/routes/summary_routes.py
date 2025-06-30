from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.doc_generator import summarize_code

router = APIRouter()

class SummarizeInput(BaseModel):
    code: str
    language: str = "python"

@router.post("/summarize/")
def summarize_route(data: SummarizeInput):
    return {"summary": summarize_code(data.code, data.language)}
