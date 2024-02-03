from dataclasses import dataclass


@dataclass
class Command:
    pass


@dataclass
class AuthenticateUserCommand(Command):
    pass


@dataclass
class CreateUser(Command):
    pass


@dataclass
class DeleteUser(Command):
    pass


@dataclass
class UpdateUser(Command):
    pass
