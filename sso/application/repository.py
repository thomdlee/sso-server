from sso.domain.model import User
from sso.domain.repository import AbstractRepository


class UserRepository(AbstractRepository):
    _fake_users_db: dict = {
        "thom": {
            "username": "thom",
            "email": "mail@thomdl.ee",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False,
        }
    }

    def add(self, model: User):
        pass

    def get(self, reference) -> User:
        if reference in self._fake_users_db:
            user_dict = self._fake_users_db[reference]

            return User(**user_dict)
