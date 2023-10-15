from di import Container, bind_by_type
from di.dependent import Dependent
from diator.container.di import DIContainer
from diator.events import EventMap, EventEmitter
from diator.mediator import Mediator
from diator.requests import RequestMap

from playground.domain.command.helloworld import HelloWorldCommandHandler, HelloWorldCommand
from playground.domain.query.greeting import GreetingQueryHandler, GreetingQuery


def bootstrap() -> Mediator:
    external_container = Container()
    container = DIContainer()
    request_map = RequestMap()

    external_container.bind(
        bind_by_type(
            Dependent(HelloWorldCommandHandler, scope="request"),
            HelloWorldCommandHandler
        )
    )

    external_container.bind(
        bind_by_type(
            Dependent(GreetingQueryHandler, scope="request"),
            GreetingQueryHandler
        )
    )

    container.attach_external_container(external_container)
    request_map.bind(HelloWorldCommand, HelloWorldCommandHandler)
    request_map.bind(GreetingQuery, GreetingQueryHandler)

    event_emitter = EventEmitter(
        event_map=EventMap(),
        container=container,
        message_broker=None
    )

    return Mediator(
        request_map=request_map,
        event_emitter=event_emitter,
        container=container
    )
