import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def ask_ollama(system_prompt, user_query):
    """
    Send a request to the local Ollama server and return the response.
    """

    prompt = f"""
System:
{system_prompt}

User:
{user_query}

Assistant:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Sorry, I couldn't generate a response."
        )

    except Exception as e:

        print("Ollama Error:", e)

        return (
            "I'm sorry, our AI assistant is currently unavailable. "
            "Please try again later."
        )
