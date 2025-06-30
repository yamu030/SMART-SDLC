from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.github_service import push_code_to_github

router = APIRouter()

class GitPushInput(BaseModel):
    code: str
    filename: str = "generated_code.py"

@router.post("/push-code/")
def push_code_route(data: GitPushInput):
    return push_code_to_github(data.code, data.filename)
