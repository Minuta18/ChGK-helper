from flask import Flask
from flask_httpauth import HTTPTokenAuth
from users import models
import secrets
from sqlalchemy import orm
import sqlalchemy
import api
import typing_extensions

models.User

class Token(api.orm_base):
    '''Token model

    Model for users' tokens.

    Attributes:
        id (int): id of the token
        user_id (int): id of the user whose token it is
        token (str): the token
    '''
    __tablename__ = 'tokens'

    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True,
    )
    user_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False,
    )
    token: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )

    @staticmethod
    def create_token(user_id: int) -> typing_extensions.Self:
        session = api.db.get_session()
        token = Token(
            user_id=user_id, 
            token=secrets.token_urlsafe(150),
        )
        session.add(token)
        session.commit()
        return token

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='bearer')