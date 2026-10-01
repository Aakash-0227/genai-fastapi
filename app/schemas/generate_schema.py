
from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="The prompt sent to the AI model"
    )


class GenerateResponse(BaseModel):
    input: str
    response: str