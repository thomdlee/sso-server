from fastapi import FastAPI

from playground.domain.query.greeting import GreetingQuery, GreetingQueryResult
from playground import bootstrap

app = FastAPI()
mediator = bootstrap.bootstrap()


@app.get("/")
async def root():
    response = await mediator.send(GreetingQuery())

    assert isinstance(response, GreetingQueryResult)

    return response.greeting
