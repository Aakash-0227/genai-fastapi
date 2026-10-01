
from fastapi import APIRouter

from app.schemas.generate_schema import (
    GenerateRequest,
    GenerateResponse,
)
from app.services.llm_service import generate_response

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    answer = generate_response(request.text)

    return GenerateResponse(
        input=request.text,
        response=answer,
    )