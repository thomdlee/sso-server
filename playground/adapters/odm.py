import abc

from playground.domain.model import User


class UserDocument(User):
    hashed_password: str


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> User:
        raise NotImplementedError
