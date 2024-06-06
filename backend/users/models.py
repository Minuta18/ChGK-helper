import sqlalchemy
import api
from sqlalchemy import orm

class User(api.orm_base):
    __tablename__ = 'users'
    
    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.BigInteger, primary_key=True,
    )
    email: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    ) 
    nickname: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )
    hashed_password: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )
