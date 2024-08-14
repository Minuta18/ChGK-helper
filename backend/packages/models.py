from sqlalchemy import orm
import sqlalchemy
import api
import typing_extensions
import questions
import users
import enum
import datetime
import typing

class PackageHardness(enum.Enum):
    easy = 'easy'
    normal = 'normal'
    hard = 'hard'
    custom = 'custom'

class SortBy(enum.Enum):
    model_id = 'id'
    created_time = 'created_time'

class PackagesToQuestions(api.orm_base):
    '''Packages model

    Table of inventory of packages

    Attributes:
        package_id (int): id of the package
        question_id (int): id of the question
    '''
    __tablename__ = 'packages_to_questions'

    package_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False,
    )
    question_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Text, nullable=False,
    )

    @staticmethod
    def get_questions_by_package_id(
        package_id: int, limit: int = 20, offset: int = 0,
    ) -> list[typing_extensions.Self]:
        '''Returns questions by package id'''
        session = api.db.get_session()
        return session.scalars(sqlalchemy.select(PackagesToQuestions).where(
            (PackagesToQuestions.package_id == package_id)
        ).limit(limit).offset(offset)).all()

class Packages(api.orm_base):
    '''Packages model

    Model for packages of our app.

    Attributes:
        id (int): id of the package
        name (str): name of the package
        description (str): short description
        user_id (int): id of the creator
    '''
    __tablename__ = 'packages'

    package_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, primary_key=True,
        autoincrement=True, unique=True,
    )
    name: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
    )
    description: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text,
    )
    creator_id: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text,
    )
    is_public: orm.Mapped[questions.models.IsPublic] = orm.mapped_column(
        nullable=False,
    )
    hardness: orm.Mapped[PackageHardness] = orm.mapped_column(
        nullable=False,
    )
    created_at: orm.Mapped[datetime.datetime] = orm.mapped_column(
        sqlalchemy.DateTime(timezone=False), nullable=False, 
        server_default=sqlalchemy.func.now()
    ) 

    '''Stores as integer. 
    
    Dont use this value, use `get_is_tournament()` and
    `set_is_tournament()` instead.
    '''
    is_tournament: orm.Mapped[int] = orm.mapped_column(
        nullable=False
    )

    def get_is_tournament(self):
        '''Return True if the package is the tournament'''
        return self.is_tournament == 1
    
    def set_is_tournament(self, is_tournament):
        '''Changes is_tournament'''
        self.is_tournament == 1 if is_tournament else 0

    def get_question_count(self):
        '''Returns the count of questions in the package.'''
        session = api.db.get_session()
        return session.scalars(session.select(
            PackagesToQuestions, sqlalchemy.func.count()
        ).where(
            (PackagesToQuestions.package_id == self.package_id)
        )).all()
    
    def get_questions(self, limit: int = 20, offset: int = 0):
        '''Returns the list of questions in the package
        
        Returns the list of questions in the package by given limit and 
        offset.

        Args:
            limit (int): The number of questions to return
            offset (int): The number of questions for start
        '''
        session = api.db.get_session()
        return session.scalars(session.select(questions.models.Question).join(
            PackagesToQuestions, (
                PackagesToQuestions.question_id == questions.models.Question.id
            )).where(
                PackagesToQuestions.package_id == self.package_id,
            ).limit(limit).offset(offset)
        ).all()

    @staticmethod
    def get_package(package_id: int) -> typing_extensions.Self | None:
        '''Returns package by id or None if it not found'''
        session = api.db.get_session()
        return session.get(Packages, package_id)
    
    @staticmethod
    def get_packages(
        limit: int = 20, offset: int = 20, by_user: int|None = None, 
        sort_by: SortBy = SortBy.created_time, reverse: bool = False,
        show_all_accessible: bool = True, show_all: bool = False,
    ) -> typing.Sequence[typing.Self]:
        '''I'm too tired to write this comment'''
        session = api.db.get_session()
        return session.scalars(session.select(Packages).join(
            users.models.User, 
            (users.models.User.id == Packages.creator_id)            
        ).where(
            ((Packages.creator_id == by_user) & (by_user is not None)) |
            ((users.models.User.permission == 
              users.models.UserPermissions.ADMIN) & (show_all_accessible)) |
            (show_all)
        ).order_by(
            (sqlalchemy.asc if not reverse else sqlalchemy.desc)(
                Packages.package_id if sort_by == SortBy.model_id 
                else Packages.created_at 
            )
        ).limit(limit).offset(offset)).all()        

    @staticmethod
    def create_package(
        creator_id: int, name: str = 'New Package', 
        description: str|None = None, 
        hardness: PackageHardness = PackageHardness.custom, 
        is_public: questions.models.IsPublic = 
        questions.models.IsPublic.private, 
    ):
        session = api.db.get_session()
        try:
            session.add(Packages(
                name=name,
                description=description,
                creator_id=creator_id,
                hardness=hardness,
                is_public=is_public,
            ))
            session.commit()
        except Exception as err:
            raise err
