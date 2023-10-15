import dataclasses
from diator.events import Event
from diator.requests import Request, RequestHandler
from diator.response import Response


@dataclasses.dataclass(frozen=True, kw_only=True)
class GreetingQuery(Request):
    pass


@dataclasses.dataclass(frozen=True, kw_only=True)
class GreetingQueryResult(Response):
    greeting: str = dataclasses.field(default=1)


class GreetingQueryHandler(RequestHandler[GreetingQuery, GreetingQueryResult]):
    def __init__(self) -> None:
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: GreetingQuery) -> GreetingQueryResult:
        return GreetingQueryResult(greeting="Hello, from another hot loaded file again! And again!")
