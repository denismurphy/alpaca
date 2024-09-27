from pydantic import BaseModel
from typing import List, Optional
from .thought import Thought

class State(BaseModel):
    thoughts: List[Thought]
    current_depth: int
    evaluation_score: Optional[float] = None