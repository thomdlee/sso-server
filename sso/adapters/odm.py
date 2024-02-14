import abc

from sso.domain.model import User


class UserDocument(User):
    hashed_password: str
