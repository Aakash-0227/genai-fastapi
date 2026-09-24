from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI(title="GenAI Day 1 API")


# Request format
class GenerateRequest(BaseModel):
    text: str


# AI function
def generate_response(text: str):

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


# POST endpoint
@app.post("/generate")
def generate(request: GenerateRequest):

    result = generate_response(request.text)

    return {
        "input": request.text,
        "response": result
    }