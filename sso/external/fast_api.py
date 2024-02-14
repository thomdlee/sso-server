from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sso import bootstrap
from sso.domain.command import LoginCommand
from sso.domain.model import User
from sso.domain.query import GetCurrentUserQuery

app = FastAPI()
mediator = bootstrap.bootstrap()


def get_password_hash(password):
    return pwd_context.hash(password)


def fake_decode_token(token):
    return get_user(fake_users_db, token)


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    await mediator.send(LoginCommand(form_data=form_data))


@app.get("/users/me/", response_model=User)
async def read_users_me():
    return await mediator.send(GetCurrentUserQuery())


@app.get("/users/me/items/")
async def read_own_items():
    response = await mediator.send(GetCurrentUserQuery())

    return [
        {
            "item_id": "Foo",
            "owner": response.username,
        }
    ]
