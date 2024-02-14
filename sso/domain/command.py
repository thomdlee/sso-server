import dataclasses
from dataclasses import dataclass

from diator.requests import Request
from diator.response import Response
from fastapi.security import OAuth2PasswordRequestForm


class Command(Request):
    pass


@dataclass(frozen=True, kw_only=True)
class LoginCommand(Command):
    token: str = dataclasses.field(default=1)
    form_data: OAuth2PasswordRequestForm = dataclasses.field(default=1)


@dataclass(frozen=True, kw_only=True)
class GetCurrentUserQueryResult(Response):
    response: dict[str, str] = dataclasses.field(default=1)
