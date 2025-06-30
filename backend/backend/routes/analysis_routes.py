from fastapi import APIRouter, UploadFile
import fitz
from backend.services.ai_story_generator import analyze_pdf_text

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    result = analyze_pdf_text(full_text)
    return result
