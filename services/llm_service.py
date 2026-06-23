from services.groq_service import ask_groq
from services.ollama_service import ask_ollama


def ask_llm(system_prompt, user_query):
    """
    Try Groq first.
    If Groq fails, automatically switch to Ollama.
    """

    try:

        print("Using Groq LLM...")

        return ask_groq(
            system_prompt=system_prompt,
            user_query=user_query
        )

    except Exception as e:

        print("Groq Failed:", e)
        print("Switching to Ollama...")

        return ask_ollama(
            system_prompt=system_prompt,
            user_query=user_query
        )
