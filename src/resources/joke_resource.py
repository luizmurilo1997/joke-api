from fastapi.routing import APIRouter
from controllers import JokeController

router = APIRouter(prefix="/api/jokes")


@router.get("/random", status_code=200)
async def get_random_joke() -> dict:
    joke_controller = JokeController()
    response = await joke_controller.get_random_joke()
    return response

@router.get("/category", status_code=200)
async def get_random_joke_by_category(category:str) -> dict:
    joke_controller = JokeController()
    response = await joke_controller.get_random_joke_by_category(category=category)
    return response

@router.get("/filter", status_code=200)
async def get_random_joke_by_filter(query:str, limit:int) -> dict:
    joke_controller = JokeController()
    response = await joke_controller.get_random_joke_by_filter(query, limit)
    return response
