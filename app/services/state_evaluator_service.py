import random
from app.models.problem import Problem
from app.models.state import State
from app.services.prompt_service import PromptService

class StateEvaluatorService:
    def __init__(self, prompt_service: PromptService):
        self.prompt_service = prompt_service

    def evaluate_state(self, problem: Problem, state: State) -> float:
        prompt = self.prompt_service.generate_evaluation_prompt(problem, state)
        # For now, we'll just return a random score
        return random.random()