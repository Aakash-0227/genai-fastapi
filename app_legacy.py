
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import ollama

# Create the FastAPI application
app = FastAPI(
    title="GenAI Day 1 API",
    description="Generate AI responses using FastAPI and Ollama",
    version="1.0.0"
)


# Request model: validates incoming data
class GenerateRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text or question to send to the AI"
    )


# Response model: defines the JSON response
class GenerateResponse(BaseModel):
    input: str
    response: str


# AI service: communicates with the local Llama model
def generate_response(text: str) -> str:
    result = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return result["message"]["content"]


# POST API endpoint
@app.post(
    "/generate",
    response_model=GenerateResponse
)
def generate(request: GenerateRequest):
    try:
        answer = generate_response(request.text)

        return GenerateResponse(
            input=request.text,
            response=answer
        )

    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail=f"AI service error: {str(error)}"
        )


# Health-check endpoint
@app.get("/")
def home():
    return {
        "message": "GenAI API is running",
        "docs": "/docs"
    }