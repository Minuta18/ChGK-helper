from sqlalchemy import orm
from passlib import context
import sqlalchemy
import api
import api.models
import typing_extensions
import re
import typing

crypt_context = context.CryptContext(
    schemes=['bcrypt'], deprecated='auto',
)

EMAIL_REGEX = api.load_regex('users/email.re')

class User(api.models.BaseModel):
    '''User model

    Model for users of our app.

    Attributes:
        id (int): id of the user
        email (str): email of the user
        nickname (str): username
        hashed_password (str): password of the user
    '''
    
    __tablename__ = 'users'
    
    email: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False, unique=True,
    )
    nickname: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
        unique=True,
    )
    hashed_password: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=True,
    )
    time_for_reading: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False, default=20
    )
    time_for_solving: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False, default=20
    )
    time_for_typing: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False, default=20
    )
    
    tokens: orm.Mapped[list['Token']] = orm.relationship(
        back_populates='parent'
    )
    
    def set_password(self, plain_password: str):
        '''Set password and hashes it
        IMPORTANT: it DO NOT commits to database! You need to use 
        session.commit MANUALLY
        '''
        self.hashed_password = crypt_context.hash(plain_password)

    def set_email(self, email: str):
        if not self.validate_email(email):
            ValueError('Invalid email')
        self.email = email
        session = api.db.get_session()
        session.add(self)
        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            raise ValueError('Email already exists')

    def verify_password(self, password: str) -> bool:
        '''Verify current password with given.
        Returns True if they are same.
        '''
        return crypt_context.verify(password, self.hashed_password, 'bcrypt')

    @staticmethod
    def validate_email(email: str) -> bool:
        '''Validate given email.

        Email is valid if it contains a valid email address according to
        wikipedia: https://en.wikipedia.org/wiki/Email_address. The main
        rules are: only digits, latin letters and printable characters are
        usable. Maximum length is 255 characters.

        Args:
            email(str): The email address

        Returns:
            bool: True if the email address is valid, False otherwise
        '''
        if len(email) < 1 and len(email) > 255:
            return False
        return re.match(EMAIL_REGEX, email)

    @staticmethod
    def validate_password(password: str) -> bool:
        '''Validate given password

        Passwords is valid if it contains only printable characters, and has
        length at least 8 characters.

        Args:
            password(str): Password to validate

        Returns:
            bool: True if password is valid, False otherwise
        '''

        if len(password) < 8 or len(password) > 255:
            return False
        # TODO
        return True

    @staticmethod
    def validate_nickname(nickname: str) -> bool:
        '''Validate nickname

        Nickname is valid if it contains at least one character and contain
        only printable characters.

        Args:
            nickname(str): Nickname to validate

        Returns:
            bool: True if nickname is valid, False otherwise
        '''
        if len(nickname) < 3 or len(nickname) > 255:
            return False
        # TODO
        return True

    @staticmethod
    def create_user(
        email: str,
        nickname: str,
        password: str
    ) -> typing_extensions.Self:
        '''Creates new user

        Args:
            email(str): The email of new user
            nickname(str): The nickname of new user
            password(str): The password of new user (plain)

        Returns:
            users.models.User: created user
        '''
        try:
            if not User.validate_email(email):
                raise ValueError('Invalid email')
            if not User.validate_password(password):
                raise ValueError('Invalid password')
            if not User.validate_nickname(nickname):
                raise ValueError('Invalid nickname')
            session = api.db.get_session()
            user = User(
                email=email,
                nickname=nickname,
            )
            session.add(user)
            session.commit()
            user.set_password(password)
            return user
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            raise ValueError('Email or Nickname already used')

    def edit(self, **kwargs) -> None:
        changeable_keys = ['time_for_reading', 'time_for_typing', 'time_for_solving']
        for key in changeable_keys:
            if kwargs.get(key) is not None:
                setattr(self, key, kwargs.get(key))
                
        something_wrong = False
        if kwargs.get('password') is not None:
            if not self.validate_password(kwargs['password']):
                something_wrong = True
            else:
                self.set_password(kwargs['password'])
                
        if kwargs.get('email') is not None:
            if not self.validate_email(kwargs['email']):
                something_wrong = True
            else:
                self.email = kwargs['email']

        if kwargs.get('nickname') is not None:
            if not self.validate_nickname(kwargs['nickname']):
                something_wrong = True
            else:
                self.nickname = kwargs['nickname']
                
        try:
            session = api.db.get_session()
            session.add(self)
            
            if something_wrong:
                session.rollback()
            else:
                session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            session.rollback()
            print(str(e))
            raise api.models.exc.ValidationError(
                'Nickname or email already used'
            )
        except Exception as e:
            session.rollback()
            raise e

    def delete(self) -> typing_extensions.Self:
        session = api.db.get_session()
        session.delete(self)
        session.commit()
        
        return self

class UserController(api.models.ModelController):
    def get_by_id(id: api.models.id_type) -> User:
        session = api.db.get_session()
        usr = session.get(User, id)
        
        if usr is None:
            raise api.models.exc.ModelNotFound
        return usr
    
    def create(**kwargs: typing.Any) -> User:
        try:
            email = kwargs['email']
            password = kwargs['password']
            nickname = kwargs['nickname']
        except IndexError:
            raise ValueError('Missed required param')
        
        try:
            if not User.validate_email(email):
                raise ValueError('Invalid email')
            if not User.validate_password(password):
                raise ValueError('Invalid password')
            if not User.validate_nickname(nickname):
                raise ValueError('Invalid nickname')
            session = api.db.get_session()
            user = User(
                email=email,
                nickname=nickname,
            )
            session.add(user)
            session.commit()
            user.set_password(password)
            return user
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            raise ValueError('Email or nickname already used')
