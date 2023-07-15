from fastapi import APIRouter
import openai
import os
#import api.schemas.gpt as gpt_schema
from typing import Optional
from pydantic import BaseModel, Field

class Info(BaseModel):
    name: Optional[str] = Field(None, example="松原健太郎")
    job: Optional[str] = Field(None, example="大学生")
    hobby: Optional[str] = Field(None, example="アニメ鑑賞、テニス、マラソン")
    money: Optional[str] = Field(None, example="40000")

router = APIRouter()
openai.api_key = "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"

@router.get("/gpt")
async def gpt_advice():
    job=os.environ.get('USERSJOB')
    hobby=os.environ.get('USERSHOBBY')
    money=os.environ.get('USERSMONEY')

    qestion="私の職業は"+job+"です。最近の趣味は"+hobby+"です。最近の趣味や職業に関連して"+money+"円程度でできる趣味を教えてください。"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": qestion},
    ],
    )
    msg = response.choices[0]["message"]["content"].strip()
    return {"advice" : msg}


@router.post("/gpt")
async def add_info(info: Info):
    os.environ['USERSNAME']=info.name
    os.environ['USERSJOB']=info.job
    os.environ['USERSHOBBY']=info.hobby
    os.environ['USERSMONEY']=info.money
    return {"res": "ok" , "name": info.name , "job": info.job ,"hobby": info.hobby ,"money":info.money}
