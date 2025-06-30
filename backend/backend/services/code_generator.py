from utils.watsonx_api import call_watsonx

MODEL_ID = "granite-20b-code-instruct"

def generate_code(user_story: str, language: str = "python"):
    prompt = f"Write a {language} function based on the following task:\n{user_story}"
    return call_watsonx(prompt, MODEL_ID)

def generate_test_case(code_snippet: str, language: str = "python"):
    prompt = f"Write unit test cases in {language} for the following code:\n{code_snippet}"
    return call_watsonx(prompt, MODEL_ID)
