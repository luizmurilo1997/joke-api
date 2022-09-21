from fastapi import FastAPI
from resources.joke_resources import router as joke_resource

description = """
A Joker é uma API JSON gratuita para fatos sobre Chuck Norris com curadoria manual.  🚀
"""

app = FastAPI(
    title="Joke API",
    description=description,
    version="0.0.1",
    
)


app.include_router(joke_resource)

