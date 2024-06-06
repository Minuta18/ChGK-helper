import sqlalchemy
import api
import typing
from sqlalchemy import orm

class User(api.orm_base):
    '''User model
    
    Model for users of our app.
    
    Attributes:
        id (int): id of the user
        email (str): email of the user
        nickname (str): username 
        hashed_password (str): password of the user
    '''
    __tablename__ = 'users'
    
    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.BigInteger, primary_key=True, 
        autoincrement=True, unique=True,
    )
    email: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
        unique=True,
    ) 
    nickname: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )
    hashed_password: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )

    @staticmethod
    def get_user(user_id: int) -> typing.Self|None:
        '''Returns user by id or None if it not found'''
        session = api.db.get_session()
        return session.get(user_id)
    
    @staticmethod
    def get_users(from_id: int = 1, to_id: int = 1) -> list[typing.Self]:
        '''Returns users with ids from from_id to to_id'''
        session = api.db.get_session()
        return session.scalars(sqlalchemy.select(User).where(
            (User.id >= from_id) & (User.id <= to_id)
        )).all()

