import dataclasses
from diator.requests import Request
from diator.response import Response


class Query:
    pass


@dataclasses.dataclass(frozen=True, kw_only=True)
class GetCurrentUserQuery(Query, Request):
    pass


@dataclasses.dataclass(frozen=True, kw_only=True)
class GetCurrentUserQueryResult(Response):
    greeting: str = dataclasses.field(default=1)
