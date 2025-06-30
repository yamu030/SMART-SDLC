from pydantic import BaseModel
from datetime import datetime

class Feedback(BaseModel):
    module: str
    input_text: str
    ai_output: str
    user_feedback: str
    timestamp: datetime = datetime.now()
