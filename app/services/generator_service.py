import random
from app.models.problem import Problem
from app.models.state import State
from app.models.thought import Thought
from app.services.prompt_service import PromptService

class GeneratorService:
    def __init__(self, prompt_service: PromptService):
        self.prompt_service = prompt_service

    def generate_thought(self, problem: Problem, state: State) -> Thought:
        prompt = self.prompt_service.generate_thought_prompt(problem, state)
        # For now, we'll just generate a random thought
        content = f"Random thought for prompt: {prompt}"
        return Thought(content=content, depth=state.current_depth + 1)

    def generate_thoughts(self, problem: Problem, state: State) -> List[Thought]:
        return [self.generate_thought(problem, state) for _ in range(problem.branching_factor)]