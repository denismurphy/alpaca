from fastapi import APIRouter, Depends
from app.models.problem import Problem
from app.models.state import State
from app.services.tree_of_thoughts_facade import TreeOfThoughtsFacade

router = APIRouter()

@router.post("/solve", response_model=State)
async def solve_problem(problem: Problem, tot_facade: TreeOfThoughtsFacade = Depends()):
    solution = tot_facade.solve(problem)
    return solution