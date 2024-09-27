from app.models.problem import Problem
from app.models.state import State
from app.services.search_service import SearchService

class TreeOfThoughtsFacade:
    def __init__(self, search_service: SearchService):
        self.search_service = search_service

    def solve(self, problem: Problem) -> State:
        return self.search_service.bfs(problem)