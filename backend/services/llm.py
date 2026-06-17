from google import generativeai as genai
from backend.config.settings import GOOGLE_API_KEY
import requests

# Gemini Configuration
genai.configure(api_key=GOOGLE_API_KEY)

gemini_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)

# Ollama Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:3b"


def has_internet() -> bool:
    """
    Check internet connectivity
    """
    try:
        requests.get(
            "https://www.google.com",
            timeout=5
        )
        return True

    except (requests.ConnectionError, requests.Timeout):
        return False

    except Exception:
        return False


def ollama_generate(prompt: str) -> str:
    """
    Generate response using Ollama
    """
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "1h"
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "No response from Ollama"
        )

    except Exception as e:
        print(f"OLLAMA ERROR: {e}")
        return "general"


def gemini_generate(prompt: str) -> str:
    """
    Generate response using Gemini
    """
    try:
        response = gemini_model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text

        return "general"

    except Exception as e:
        print(f"GEMINI ERROR: {e}")
        return "general"


def invoke(message: str) -> str:
    """
    Main LLM Router
    Uses Gemini if internet exists.
    Otherwise uses Ollama.
    """

    if has_internet():

        print("USING GEMINI")

        return gemini_generate(message)

    else:

        print("NO INTERNET! USING OLLAMA")

        return ollama_generate(message)