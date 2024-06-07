import sqlalchemy
import api
from sqlalchemy import orm

class Question(api.orm_base):
    '''Class for questions

    Creates a table for questions that have an id, the question's text and
    optionally a comment
    
    '''
    __tablename__ = 'questions'

    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.BigInteger, primary_key=True,
    )
    text: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String, nullable=False,
    )
    comment: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String,
    )
