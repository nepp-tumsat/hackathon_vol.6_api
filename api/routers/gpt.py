from fastapi import APIRouter

import openai

router = APIRouter()

@router.get("/gpt")
async def gpt_advice():
    pass


@router.post("/gpt")
async def add_info():
    pass

