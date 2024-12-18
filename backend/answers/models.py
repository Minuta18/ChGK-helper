from sqlalchemy import orm
from shared_library import strings
import api.models
import sqlalchemy
import api
import typing_extensions
import typing

class Answer(api.models.BaseModel):
    '''Answer model
    
    Model for users of our app.
    
    Attributes:
        id (int): id of the answer
        question_id (int): id of the question
        correct_answer (str): correct answer
    '''
    
    __tablename__ = 'answers'
    
    question_id: orm.Mapped[api.models.id_type] = orm.mapped_column(
        sqlalchemy.ForeignKey('questions.id')
    )
    question: orm.Mapped['Question'] = orm.relationship(
        back_populates='children'
    )
    correct_answer: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text, nullable=False,
    )
    raw_correct_answer: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text, nullable=False,
    )

    def set_correct_answer(self, raw_correct_answer: str):
        '''Parses raw correct answer and writes it to model
        
        IMPORTANT: This method DOES NOT commits the changes, so you need to do
        it MANUALLY
        '''
        
        self.raw_correct_answer = raw_correct_answer
        cleaner = strings.TextCleaner()
        cleaner.set_strategy(strings.HardCleanStrategy())
        self.correct_answer = cleaner.clean(self.raw_correct_answer)

    @staticmethod
    def create(
        question_id: int = ..., correct_answer: str = ...
    ) -> typing_extensions.Self:
        '''create new answer with question_ia and correct_answer'''
        
        assert question_id != ..., 'question_id is required'
        assert correct_answer != ..., 'correct_answer is required'
        
        session = api.db.get_session()
        cleaner = strings.TextCleaner()
        cleaner.set_strategy(strings.HardCleanStrategy())
        answer = Answer(
            question_id=question_id, 
            raw_correct_answer=correct_answer,
            correct_answer=cleaner.clean(correct_answer),
        )
        session.add(answer)
        session.commit()
        return answer

    def delete_answer(self) -> typing_extensions.Self:
        '''delete existing answer by id'''
        session = api.db.get_session()
        session.delete(self)
        session.commit()
        
        return self

    def edit(self, **kwargs: dict[str, typing.Any]) -> None:
        '''Edits answer
        
        Edits answer as said in `kwargs`. (In fact there is only one param:
        `correct_answer`.
        '''
        
        new_text = kwargs.get('correct_answer')
        if new_text is not None:
            self.set_correct_answer(new_text)
        
        session = api.db.get_session()
        session.add(self)
        session.commit()

    def check_answer(self, answer: str):
        '''check if answer is correct or not'''
        cleaner = strings.TextCleaner()
        cleaner.set_strategy(strings.HardCleanStrategy())
        checker = strings.AnswerChecker()
        return checker.check_answer(
            cleaner.clean(answer),
            self.correct_answer,
        )

class AnswerController(api.models.ModelController):
    '''AnswerController
    
    AnswerController is a class which implements TNO REFERENCE
    '''
    
    def get_by_id(model_id: api.models.id_type) -> Answer:
        session = api.db.get_session()
        ans = session.get(Answer, model_id)
        
        if ans is None:
            raise api.models.exc.ModelNotFound
        return ans
    
    def create(**kwargs: typing.Any) -> Answer:
        return Answer.create(**kwargs)
