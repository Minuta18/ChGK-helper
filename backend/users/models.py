from sqlalchemy import orm
import sqlalchemy
import api
import typing
import passlib
import re

crypt_context = passlib.context.CryptContext(
    schemas=['bcrypt'], deprecated='auto'
)

EMAIL_REGEX = api.load_regex('users/email.re')

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

    def set_password(self, plain_password: str):
        '''Set password and hashes it'''
        self.hashed_password = crypt_context.hash(plain_password)

    def verify_password(self, password: str) -> bool:
        '''Verify current password with given. 
        Returns True if they are same.
        '''
        return crypt_context.verify(self.hashed_password, password)

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
        
        if len(password) < 9 or len(password) > 255: return False
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
        if len(nickname) < 1 or len(nickname) > 255: return False
        # TODO
        return True

    @staticmethod
    def get_user(user_id: int) -> typing.Self|None:
        '''Returns user by id or None if it not found'''
        session = api.db.get_session()
        return session.get(user_id)
    
    @staticmethod
    def get_users(from_id: int = 1, to_id: int = 1) -> list[typing.Self]:
        '''Returns users with ids from from_id to to_id'''
        session = api.db.get_session()
        return session.scalars(sqlalchemy.select(User).where(
            (User.id >= from_id) & (User.id <= to_id)
        )).all() 
        
    @staticmethod
    def create_user(email: str, nickname: str, password: str) -> typing.Self:
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
            user = User(email=email, nickname=nickname)
            user.set_password(password)
            session.add(user)
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            raise ValueError('Email already used')
        
