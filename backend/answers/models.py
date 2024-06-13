from sqlalchemy import orm
import sqlalchemy
import api
import typing_extensions
import passlib

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
        sqlalchemy.Integer, primary_key=True, 
        autoincrement=True, unique=True,
    )
    question_id: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.BigInteger, unique=True,
    )
    correct_answer: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )

    @staticmethod
    def get_answer(answer_id: int) -> typing_extensions.Self|None:
        '''Returns answer by id or None if it not found'''
        session = api.db.get_session()
        return session.get(Answer, answer_id)
    
    @staticmethod
    def get_answers(from_id: int, to_id: int) -> list[typing_extensions.Self]:
        '''Returns answers with ids from from_id to to_id'''
        session = api.db.get_session()
        return session.scalars(sqlalchemy.select(Answer).where(
            (Answer.id >= from_id) & (Answer.id <= to_id)
        )).all()

    @staticmethod
    def create_answer(
        question_id: int, correct_answer: str
    ) -> typing_extensions.Self:
        '''create new answer with question_ia and correct_answer'''
        session = api.db.get_session()
        answer = Answer(question_id=question_id, correct_answer=correct_answer)
        session.add(answer)
        session.commit()
        return answer

    @staticmethod
    def delete_answer(answer_id: int) -> None:
        '''delete existful answer by id'''
        answer = Answer.get_answer(answer_id)
        if answer is None:
            raise ValueError('User not found')
        session = api.db.get_session()
        session.delete(answer)
        session.commit()

    def update_answer(self, question_id: int = None, correct_answer: str = None):
        '''change question_id and correct_answer of choosen answer'''
        if question_id is not None:
            self.question_id = question_id
        if correct_answer is not None:
            self.correct_answer = correct_answer
        session = api.db.get_session()
        session.add(self)
        session.commit()
        return self

    def check_answer(self, answer: str):
        '''check what answer is correct or not'''
        if self.correct_answer.lower.split() == answer.lower().split():
            return True
        else:
            return False

    @staticmethod
    def get_answer_by_question(
        question_id: int
    ) -> typing_extensions.Self|None:
        '''Returns answer by question_id or None if it not found'''
        session = api.db.get_session()
        return session.get(Answer, question_id)
