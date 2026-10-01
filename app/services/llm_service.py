
import ollama


def generate_response(text: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response["message"]["content"]