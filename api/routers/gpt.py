from fastapi import APIRouter
import os
import openai

router = APIRouter()
openai.api_key_path = "./.apikey"

@router.get("/gpt")
async def gpt_advice():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "お勧めの気晴らしは？"},
    ],
    )
    return response.choices[0]["message"]["content"].strip()


@router.post("/gpt")
async def add_info():
    pass

