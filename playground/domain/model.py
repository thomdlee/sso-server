from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None
    hashed_password: str


class Guest(User):
    pass


class Staff(User):
    pass


class Admin(User):
    pass
