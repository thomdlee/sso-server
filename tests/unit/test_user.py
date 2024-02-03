from playground.domain.model import User


def test_user_authentication():
    user = User()

    user.authenticate()
