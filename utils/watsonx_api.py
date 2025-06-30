import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
BASE_URL = os.getenv("WATSONX_BASE_URL")

def call_watsonx(prompt, model_id):
    url = f"{BASE_URL}/ml/v1/text/generation"  # ✅ Correct Watsonx endpoint

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model_id": model_id,
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200,
        },
        "project_id": PROJECT_ID,
    }

    response = requests.post(url, headers=headers, json=payload)

    # ✅ DEBUG LOGGING ADDED HERE
    print("Watsonx API Response:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    try:
        result = response.json()["results"][0]["generated_text"]
        return result
    except Exception as e:
        return f"Error: {e}\nFull Response: {response.text}"
