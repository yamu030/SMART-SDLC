from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from backend.services.ai_story_generator import analyze_pdf_text
import fitz  # PyMuPDF

app = FastAPI(title="SmartSDLC Requirement Analyzer")

# Enable CORS so frontend can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only. Restrict in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def home():
    return {"message": "SmartSDLC Backend Running ✅"}

# Upload and analyze PDF
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    result = analyze_pdf_text(full_text)
    return result
