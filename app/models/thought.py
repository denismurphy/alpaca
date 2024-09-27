from pydantic import BaseModel
from typing import Optional, List

class Thought(BaseModel):
    content: str
    depth: int
    parent: Optional['Thought'] = None
    children: List['Thought'] = []
    evaluation_score: Optional[float] = None