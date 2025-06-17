from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='wan', email='wan@wan.com', password='minha_senha')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'wan@wan.com'))

    assert result.id == 1
