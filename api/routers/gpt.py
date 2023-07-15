from fastapi import APIRouter
import os
import openai

router = APIRouter()
openai.api_key = os.getenv("OPENAI_API_KEY")

@router.get("/gpt")
async def gpt_advice():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "お勧めの気分転換は？"},
    ],
    )
    return response.choices[0]["message"]["content"].strip()


@router.post("/gpt")
async def add_info():
    pass

