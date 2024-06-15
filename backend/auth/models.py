from flask import Flask
from flask_httpauth import HTTPTokenAuth
from users import models
import secrets
from sqlalchemy import orm
import sqlalchemy
import api
import typing_extensions

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
            given_id=user_id,
            token=secrets.token_urlsafe(150),
        )
        session.add(token)
        session.commit()
        return token

    @staticmethod
    def delete_token(given_id: int) -> None:
        '''Deletes user's token by given id'''
        session = api.db.get_session()
        to_delete = session.scalars(
            sqlalchemy.select(
                Token
                ).where(
                    Token.user_id == given_id
                )
            ).all()
        for i in to_delete:
            session.delete(i)

    @staticmethod
    def get_user_by_token(token: str) -> typing_extensions.Self:
        '''Gets a user by a given token'''
        session = api.db.get_session()
        try:
            peremenaya = session.scalars(sqlalchemy.select(
                    Token
                ).where(Token.token == token)
            ).all()[0]
        except IndexError:
            return None
        return models.User.get_user(peremenaya.user_id)
    