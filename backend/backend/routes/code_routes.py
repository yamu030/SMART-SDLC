from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.code_generator import generate_code, generate_test_case

router = APIRouter()

class CodeInput(BaseModel):
    prompt: str
    language: str = "python"

@router.post("/generate-code/")
def generate_code_route(data: CodeInput):
    return {"generated_code": generate_code(data.prompt, data.language)}

@router.post("/generate-test/")
def generate_test_case_route(data: CodeInput):
    return {"generated_test": generate_test_case(data.prompt, data.language)}
