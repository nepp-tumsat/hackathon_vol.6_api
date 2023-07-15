from typing import Optional

from pydantic import BaseModel, Field

class Task(BaseModel):
    mane: Optional[str] = Field(None, example="松原健太郎")
    job: Optional[str] = Field(None, example="大学生")
    hoby: Optional[str] = Field(None, example="")
    id: int
