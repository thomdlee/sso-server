from datetime import timedelta
from typing import Dict

from diator.events import Event
from diator.requests import RequestHandler
from fastapi import HTTPException, status
from passlib.context import CryptContext

from sso.domain.command import LoginCommand
from sso.domain.model import User
from sso.domain.query import GetCurrentUserQuery, GetCurrentUserQueryResult
from sso.domain.service import UserService


class LoginCommandHandler(RequestHandler[LoginCommand, None]):
    user_service: UserService
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: LoginCommand) -> Dict[str, str]:
        form_data = LoginCommand.form_data
        user = self.user_service.authenticate_user(
            form_data.username, form_data.password
        )

        self._throw_http_exception_on_invalid_user(user)

        access_token_expires = timedelta(minutes=self._ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}

    def _throw_http_exception_on_invalid_user(self, user: User | None):
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )


class GetCurrentUserQueryHandler(RequestHandler[GetCurrentUserQuery, None]):
    _SECRET_KEY = "442b8be1737adb9d4e298ab9535b053e6e7181df39ed1e135c6609e418d95a74"
    _ALGORITHM = "HS256"

    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: LoginCommand) -> GetCurrentUserQueryResult:
        current_user = self.get_current_user(request.token)

        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")

        return current_user
