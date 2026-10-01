
from fastapi import FastAPI
from app.routes.generate import router as generate_router

app = FastAPI(
    title="GenAI API",
    description="A modular API using FastAPI and Ollama",
    version="1.0.0",
)

app.include_router(generate_router)


@app.get("/")
def home():
    return {"message": "GenAI API is running"}