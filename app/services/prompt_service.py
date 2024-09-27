from app.models.problem import Problem
from app.models.state import State

class PromptService:
    def generate_thought_prompt(self, problem: Problem, state: State) -> str:
        return f"Given the problem: '{problem.input}' and the current state: '{state.thoughts[-1].content if state.thoughts else ''}', generate a new thought."

    def generate_evaluation_prompt(self, problem: Problem, state: State) -> str:
        return f"Given the problem: '{problem.input}' and the current state: '{state.thoughts[-1].content if state.thoughts else ''}', evaluate the quality of this state on a scale from 0 to 1."