from utils.watsonx_api import call_watsonx

def analyze_pdf_text(text: str):
    model_id = "granite-13b-chat-v1"
    classified = call_watsonx(text, model_id)

    user_stories = []
    for line in classified.split("\n"):
        if "Requirement" in line:
            story = f"As a user, I want {line.split(':')[-1].strip()} so that it meets the requirement."
            user_stories.append(story)

    return {
        "classified_text": classified,
        "user_stories": user_stories
    }



