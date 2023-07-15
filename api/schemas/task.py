from typing import Optional

from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    limit: Optional[str] = Field(None, example="YYYY-MM-DD")
    done: bool = Field(False, description="完了フラグ")
