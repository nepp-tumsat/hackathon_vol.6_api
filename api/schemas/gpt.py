from typing import Optional

from pydantic import BaseModel, Field

class Info(BaseModel):
    name: Optional[str] = Field(None, example="松原健太郎")
    job: Optional[str] = Field(None, example="大学生")
    hobby: Optional[str] = Field(None, example="アニメ鑑賞、テニス、マラソン")
    money: Optional[str] = Field(None, example="40000")
