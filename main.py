from fastapi import FastAPI

from application.query.greeting import GreetingQuery, GreetingQueryResult
from presentation import server

app = FastAPI()
# todo: we don't want the mediator creation code to run on every request :(


@app.get("/")
async def goto_root():
    mediator = await server.mediator()
    response = await mediator.send(GreetingQuery())

    assert isinstance(response, GreetingQueryResult)

    return response.greeting
