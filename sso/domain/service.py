from datetime import timedelta, datetime

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from sso.domain.model import TokenData, User
from sso.domain.repository import AbstractRepository


class DomainService:
    pass


class UserService(DomainService):
    _repository: AbstractRepository
    _SECRET_KEY = "442b8be1737adb9d4e298ab9535b053e6e7181df39ed1e135c6609e418d95a74"
    _ALGORITHM = "HS256"
    _ACCESS_TOKEN_EXPIRE_MINUTES = 30
    _credentials_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    def get_user(self, username: str):
        pass

    def verify_password(self, plaintext, hashed_text):
        return self._pwd_context.verify(plaintext, hashed_text)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self._SECRET_KEY, algorithm=self._ALGORITHM)

        return encoded_jwt

    async def get_current_user(self, token: str):
        oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

        try:
            payload = jwt.decode(token, self._SECRET_KEY, algorithms=[self._ALGORITHM])
            username: str = payload.get("sub")

            if username is None:
                raise self._credentials_exception

            token_data = TokenData(username=username)
        except JWTError:
            raise self._credentials_exception

        user = self.get_user(username=token_data.username)

        self._throw_exception_for_invalid_user(user)

        return user

    def _throw_exception_for_invalid_user(self, user):
        if user is None:
            raise self._credentials_exception

    def authenticate_user(self, username: str, password: str) -> User | bool:
        user = self._repository.get(username)

        if not user:
            return False

        if not self.verify_password(password, user.hashed_password):
            return False

        return user
