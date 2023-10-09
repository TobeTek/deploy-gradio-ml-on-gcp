import requests
import os
from typing import Optional

HUGGING_FACE_TOKEN = os.environ["HUGGING_FACE_TOKEN"]
MODEL_API_URL = (
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
)

headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}


def query(payload: Optional[dict] = None, inputs: Optional[str] = None):
    if payload is None:
        payload = {
            "inputs": inputs,
            "parameters": {
                "max_new_tokens": 240,
                "return_full_text": False,
            },
            "options": {"use_cache": True, "wait_for_model": True},
        }
    response = requests.post(MODEL_API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]
