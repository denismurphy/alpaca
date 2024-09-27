from pydantic import BaseModel

class Problem(BaseModel):
    input: str
    max_depth: int
    branching_factor: int
    evaluation_threshold: float