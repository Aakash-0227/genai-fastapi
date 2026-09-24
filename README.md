# GenAI FastAPI API - Day 1

## Project Overview

This project demonstrates how a Generative AI model can be exposed through a REST API using FastAPI.

The application accepts a text prompt through a POST API endpoint, sends the prompt to the Llama 3.2 Large Language Model through Ollama, and returns the generated response as JSON.

## Architecture

User
↓
POST /generate
↓
FastAPI
↓
Ollama
↓
Llama 3.2
↓
Generated Response
↓
JSON Response

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Ollama
- Llama 3.2
- REST API
- JSON

## API Endpoint

### POST /generate

Accepts a text prompt and generates an AI response.

### Request

```json
{
    "text": "Explain artificial intelligence in simple terms"
}