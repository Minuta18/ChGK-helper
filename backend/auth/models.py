from users import models
import secrets
from sqlalchemy import orm
import sqlalchemy
import api
import api.models
import typing_extensions

TOKEN_LENGTH = 75

class Token(api.orm_base):
    '''Token model

    Model for users' tokens.

    Attributes:
        id (id_type): id of the token
        user_id (id_type): id of the user whose token it is
        token (str): the token
    '''
    __tablename__ = 'tokens'

    id: orm.Mapped[api.models.id_type] = orm.mapped_column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True,
    )
    user_id: orm.Mapped[api.models.id_type] = orm.mapped_column(
        sqlalchemy.ForeignKey('users.id'), nullable=False,
    )
    user: orm.Mapped['User'] = orm.relationship(
        back_populates='children'
    )
    token: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )

    @staticmethod
    def _generate_token() -> str:
        return secrets.token_urlsafe(TOKEN_LENGTH)

    @staticmethod
    def create_token(user_id: int) -> typing_extensions.Self:
        session = api.db.get_session()
        token = Token(
            user_id=user_id,
            token=Token._generate_token(),
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

    def find_token(token: str) -> typing_extensions.Self:
        '''Returns token instance by string'''
        session = api.db.get_session()
        try:
            return session.scalars(
                sqlalchemy.select(Token).where(Token.token == token)    
            ).all()[0]
        except IndexError: return None

    def get_user(self) -> typing_extensions.Self:
        '''Returns user'''
        return self.user 
