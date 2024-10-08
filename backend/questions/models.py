import sqlalchemy
import api
from sqlalchemy import orm
import typing_extensions
import enum

class IsPublic(enum.Enum):
    private = 'private'
    public = 'public'

class Question(api.orm_base):
    '''Class for questions

    Creates a table for questions that have an id, the question's text and
    optionally a comment

    '''
    __tablename__ = 'questions'

    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    text: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String, nullable=False,
    )
    comment: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String,
    )
    visibility: orm.Mapped[IsPublic] = orm.mapped_column(
        nullable=False,
    )
    creator_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False,
    )

    @staticmethod
    def get_question(question_id: int) -> typing_extensions.Self | None:
        '''Returns question by id or None if user not found'''
        session = api.db.get_session()
        return session.get(Question, question_id)

    @staticmethod
    def get_questions(
        from_id: int = 1, to_id: int = 1, allow_private: bool = True,
    ) -> list[typing_extensions.Self]:
        '''Returns questions with ids from from_id to to_id'''
        session = api.db.get_session()
        if not allow_private:
            return session.scalars(sqlalchemy.select(Question).where(
                (Question.id >= from_id) & (Question.id <= to_id) 
                & (Question.public == IsPublic.public)
            )).all()
        return session.scalars(sqlalchemy.select(Question).where(
            (Question.id >= from_id) & (Question.id <= to_id)
        )).all()

    @staticmethod
    def add_question(
        text: str, comment: str, visibility: IsPublic,
        creator_id: int, 
    ) -> typing_extensions.Self:
        '''Adds a new question

        Args:
            text(str): The question's text
            comment(str, optional): A comment to the question

        Returns:
            questions.models.Question: created question
        '''

        session = api.db.get_session()
        question = Question(
            text=text, comment=comment, visibility=visibility, 
            creator_id=creator_id, 
        )
        session.add(question)
        session.commit()
        return question

    @staticmethod
    def delete_question(question_id) -> typing_extensions.Self:
        '''Deletes the question by given id'''

        question = Question.get_question(question_id)
        if question is None:
            raise ValueError('Question not found')
        session = api.db.get_session()
        session.delete(question)
        session.commit()
