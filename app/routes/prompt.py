from fastapi import APIRouter, HTTPException, status

from app.schemas.prompt_schema import PromptCreate, PromptUpdate

router = APIRouter(prefix="/prompts", tags=["Prompt Management"])

# Temporary in-memory storage
prompts = {}
next_prompt_id = 1


# GET: Retrieve all prompts
@router.get("/")
def get_prompts():
    return list(prompts.values())


# GET: Retrieve one prompt by ID
@router.get("/{prompt_id}")
def get_prompt(prompt_id: int):
    if prompt_id not in prompts:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found"
        )

    return prompts[prompt_id]


# POST: Create a new prompt
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_prompt(prompt: PromptCreate):
    global next_prompt_id

    prompt_id = next_prompt_id

    new_prompt = {
        "id": prompt_id,
        "title": prompt.title,
        "text": prompt.text
    }

    prompts[prompt_id] = new_prompt
    next_prompt_id += 1

    return new_prompt


# PUT: Replace an existing prompt
@router.put("/{prompt_id}")
def update_prompt(prompt_id: int, prompt: PromptUpdate):
    if prompt_id not in prompts:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found"
        )

    updated_prompt = {
        "id": prompt_id,
        "title": prompt.title,
        "text": prompt.text
    }

    prompts[prompt_id] = updated_prompt

    return updated_prompt


# DELETE: Delete a prompt
@router.delete("/{prompt_id}")
def delete_prompt(prompt_id: int):
    if prompt_id not in prompts:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found"
        )

    deleted_prompt = prompts.pop(prompt_id)

    return {
        "message": "Prompt deleted successfully",
        "deleted_prompt": deleted_prompt
    }