import abc

from pydantic import BaseModel


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model: BaseModel):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> BaseModel:
        raise NotImplementedError
