from sqlalchemy import orm
import typing_extensions
import sqlalchemy
import typing
import api.models
import api

class Question(api.models.BaseModel):
    '''Class for questions

    Creates a table for questions that have an id, the question's text and
    optionally a comment

    '''
    
    __tablename__ = 'questions'

    text: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String, nullable=False,
    )
    comment: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String,
    )
    creator_id: orm.Mapped[api.models.id_type] = orm.mapped_column(
        sqlalchemy.ForeignKey('users.id'), nullable=False,
    )
    creator: orm.Mapped['User'] = orm.relationship(back_populates='children')
    
    answers: orm.Mapped[typing.List['Answer']] = orm.relationship(
        back_populates='parent'
    )

    @staticmethod
    def create(
        text: str = ..., comment: str|None = None,
        creator_id: int = ..., 
    ) -> typing_extensions.Self:
        '''Adds a new question

        Args:
            text(str): The question's text
            comment(str, optional): A comment to the question
            creator_id(int)

        Returns:
            questions.models.Question: created question
        '''
        
        assert text != ..., 'text is required'
        assert creator_id != ..., 'creator_id is required'

        session = api.db.get_session()
        question = Question(
            text=text, comment=comment, 
            creator_id=creator_id, 
        )
        session.add(question)
        session.commit()
        return question
    
    def edit(self, **kwargs: dict[str, typing.Any]) -> None:
        changeable_keys = ['text', 'comment']
        for key in changeable_keys:
            if kwargs.get(key) is not None:
                setattr(self, key, kwargs.get(key))
        
        session = api.db.get_session()
        session.add(self)
        session.commit()
        
    def delete(self) -> typing_extensions.Self:
        session = api.db.get_session()
        session.delete(self)
        session.commit()
        
        return self

class QuestionController(api.models.ModelController):
    '''QuestionController
    
    во-вторых я НЕ буду работать с докером. Даже после твоих лекций, даже после
    ПЯТИ(!!!) гугл-запросов я не понял нихрена кроме самой сути программы и 
    того что такое dockerfile. 
    И в-третьих блин, если то, что тебе надо дописать, не касается дальнейшего 
    написания кода, то СДЕЛАЙ ПУЛ РЕКВЕСТ СТЕАПИЩЕ ТЫ НЕДОДЕЛАННОЕ
    (c) Ivun Levkov
    '''
    
    def get_by_id(model_id: api.models.id_type) -> Question:
        session = api.db.get_session()
        model = session.get(Question, model_id)
        
        if model is None:
            raise api.models.exc.ModelNotFound
        return model
    
    def create(**kwargs: typing.Any) -> Question:
        return Question.create(**kwargs)
