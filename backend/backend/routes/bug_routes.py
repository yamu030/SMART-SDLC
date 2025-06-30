from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.bug_resolver import fix_bug

router = APIRouter()

class BugInput(BaseModel):
    code: str
    language: str = "python"

@router.post("/fix-bug/")
def fix_bug_route(data: BugInput):
    return {"fixed_code": fix_bug(data.code, data.language)}
