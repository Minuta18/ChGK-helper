from sqlalchemy import orm
import sqlalchemy
import api
import typing
import passlib

context = passlib.context()

class Answer(api.orm_base):
    '''User model
    
    Model for users of our app.
    
    Attributes:
        id (int): id of the answer
        question_id (int): id of the question
        correct_answer (str): correct answer
    '''
    __tablename__ = 'answers'
    
    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.BigInteger, primary_key=True, 
        autoincrement=True, unique=True,
    )
    question_id: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.BigInteger, unique=True,
    )
    correct_answer: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )

    @staticmethod
    def get_answer(answer_id: int) -> typing.Self|None:
        '''Returns answer by id or None if it not found'''
        session = api.db.get_session()
        return session.get(answer_id)
    
    @staticmethod
    def get_answers(from_id: int, to_id: int) -> list[typing.Self]:
        '''Returns answers with ids from from_id to to_id'''
        session = api.db.get_session()
        return session.scalars(sqlalchemy.select(Answer).where(
            (Answer.id >= from_id) & (Answer.id <= to_id)
        )).all()

    @staticmethod
    def create_answer(question_id: int, correct_answer: str) -> typing.Self:
        ''''''
        session = api.db.get_session()
        answer = Answer(question_id=question_id, correct_answer=correct_answer)
        session.add(answer)
        session.commit()
        return answer

    @staticmethod
    def delete_answer(answer_id: int) -> None:
        ''''''
        answer = Answer.get_answer(answer_id)
        if answer is None:
            raise ValueError('User not found')
        session = api.db.get_session()
        session.delete(answer)
        session.commit()

    def update_answer(self, question_id: int, correct_answer: str):
        ''''''
        self.question_id = question_id
        self.correct_answer = correct_answer
        session = api.db.get_session()
        session.add(self)
        session.commit()
        return self
