from utils.watsonx_api import call_watsonx

MODEL_ID = "granite-20b-code-instruct"

def fix_bug(code: str, language: str = "python"):
    prompt = f"Fix any syntax or logic errors in this {language} code:\n{code}"
    return call_watsonx(prompt, MODEL_ID)
