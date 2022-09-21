from fastapi import FastAPI
from resources.joke_resource import router as joke_resource

description = """
A Joke é uma API REST gratuita que disponibiliza piadas sobre a vida de chuck norris.  🚀
"""

app = FastAPI(
    title="Joke API",
    description=description,
    version="0.0.2",
    
)


app.include_router(joke_resource)

