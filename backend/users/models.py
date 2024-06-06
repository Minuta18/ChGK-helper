import sqlalchemy
import api
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
