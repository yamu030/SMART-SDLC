from utils.watsonx_api import call_watsonx

MODEL_ID = "granite-20b-code-instruct"

def summarize_code(code: str, language: str = "python"):
    prompt = f"Explain what the following {language} code does:\n{code}"
    return call_watsonx(prompt, MODEL_ID)
