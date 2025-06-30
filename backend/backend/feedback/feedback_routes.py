from fastapi import APIRouter
from backend.feedback.feedback_model import Feedback

router = APIRouter()
feedback_store = []

@router.post("/feedback/")
def submit_feedback(feedback: Feedback):
    feedback_store.append(feedback)
    return {"message": "Feedback received!"}

@router.get("/feedback/")
def get_all_feedback():
    return feedback_store
