from typing import List
from collections import deque
from app.models.problem import Problem
from app.models.state import State
from app.models.thought import Thought
from app.services.generator_service import GeneratorService
from app.services.state_evaluator_service import StateEvaluatorService

class SearchService:
    def __init__(self, generator_service: GeneratorService, evaluator_service: StateEvaluatorService):
        self.generator_service = generator_service
        self.evaluator_service = evaluator_service

    def bfs(self, problem: Problem) -> State:
        initial_state = State(thoughts=[], current_depth=0)
        queue = deque([initial_state])

        best_state = initial_state
        best_score = 0

        while queue:
            current_state = queue.popleft()

            if current_state.current_depth >= problem.max_depth:
                continue

            new_thoughts = self.generator_service.generate_thoughts(problem, current_state)
            for thought in new_thoughts:
                new_state = State(
                    thoughts=current_state.thoughts + [thought],
                    current_depth=current_state.current_depth + 1
                )
                new_state.evaluation_score = self.evaluator_service.evaluate_state(problem, new_state)

                if new_state.evaluation_score > best_score:
                    best_state = new_state
                    best_score = new_state.evaluation_score

                if new_state.evaluation_score >= problem.evaluation_threshold:
                    return new_state

                queue.append(new_state)

        return best_state