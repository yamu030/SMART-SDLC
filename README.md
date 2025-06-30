
✅ `README.md` (Simple & Understandable)

SmartSDLC – AI-Powered SDLC Automation

SmartSDLC is a mini AI-based platform that helps automate parts of the software development lifecycle using FastAPI, Streamlit, and IBM Watsonx.

✅ Features Done So Far

- Upload PDF requirements
- AI classifies text into SDLC phases (like Requirements, Design)
- Converts them into user stories
- Backend built with FastAPI
- Frontend built with Streamlit
- IBM Watsonx integration using Granite models

🛠 Tech Stack

- Python 3.10
- FastAPI
- Streamlit
- IBM Watsonx
- PyMuPDF
- LangChain (planned)
- Uvicorn

📁 Project Structure

SmartSDLC/
├── backend/
├── frontend/
├── .env
├── requirements.txt


🚀 How to Run
Create virtual environment
python3 -m venv env
source env/bin/activate

Install requirements
pip install -r requirements.txt
Run backend
uvicorn backend.main:app --reload
Run frontend
streamlit run frontend/app.py
