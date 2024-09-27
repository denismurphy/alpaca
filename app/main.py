from fastapi import FastAPI
from app.api.routes.routes import router
from app.services.prompt_service import PromptService
from app.services.generator_service import GeneratorService
from app.services.state_evaluator_service import StateEvaluatorService
from app.services.search_service import SearchService
from app.services.tree_of_thoughts_facade import TreeOfThoughtsFacade

app = FastAPI()

app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    prompt_service = PromptService()
    generator_service = GeneratorService(prompt_service)
    evaluator_service = StateEvaluatorService(prompt_service)
    search_service = SearchService(generator_service, evaluator_service)
    tot_facade = TreeOfThoughtsFacade(search_service)

    app.state.tot_facade = tot_facade

def get_tot_facade():
    return app.state.tot_facade

app.dependency_overrides[TreeOfThoughtsFacade] = get_tot_facade