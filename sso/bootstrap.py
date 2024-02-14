from di import Container, bind_by_type
from di.dependent import Dependent
from diator.container.di import DIContainer
from diator.events import EventMap, EventEmitter
from diator.mediator import Mediator
from diator.requests import RequestMap

from sso.application.handler import LoginCommandHandler
from sso.domain.command import LoginCommand


def bootstrap() -> Mediator:
    external_container = Container()
    container = DIContainer()
    request_map = RequestMap()

    bind_handlers(request_map, external_container)
    container.attach_external_container(external_container)

    event_emitter = get_event_emitter(container)

    return Mediator(
        request_map=request_map,
        event_emitter=event_emitter,
        container=container,
    )


def get_event_emitter(container: DIContainer) -> EventEmitter:
    return EventEmitter(
        event_map=EventMap(),
        container=container,
        message_broker=None,
    )


def bind_handlers(request_map: RequestMap, external_container: Container) -> None:
    request_map.bind(LoginCommand, LoginCommandHandler)
    external_container.bind(
        bind_by_type(
            Dependent(LoginCommandHandler, scope="request"),
            LoginCommandHandler,
        )
    )
