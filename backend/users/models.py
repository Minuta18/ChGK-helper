from sqlalchemy import orm
from passlib import context
import sqlalchemy
import api
import typing
import typing_extensions
import re
import enum

crypt_context = context.CryptContext(
    schemes=['bcrypt'], deprecated='auto',
)

EMAIL_REGEX = api.load_regex('users/email.re')

class UserPermissions(enum.Enum):
    DEFAULT = 0
    ADMIN = 1

def user_permissions_to_string(user_permissions: UserPermissions):
    return 'admin' if user_permissions == UserPermissions.ADMIN else 'default'

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
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    email: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
        unique=True,
    )
    nickname: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=False,
        unique=True,
    )
    hashed_password: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(255), nullable=True,
    )
    permission: orm.Mapped[UserPermissions] = orm.mapped_column(
        nullable=False
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

    def set_password(self, plain_password: str):
        '''Set password and hashes it'''
        self.hashed_password = crypt_context.hash(plain_password)
        session = api.db.get_session()
        session.add(self)
        session.commit()

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
        if len(nickname) < 1 or len(nickname) > 255:
            return False
        # TODO
        return True

    @staticmethod
    def get_user(user_id: int) -> typing_extensions.Self | None:
        '''Returns user by id or None if it not found'''
        session = api.db.get_session()
        return session.get(User, user_id)

    @staticmethod
    def get_users(
        from_id: int = 1, to_id: int = 1
    ) -> list[typing_extensions.Self]:
        '''Returns users with ids from from_id to to_id'''
        try:
            session = api.db.get_session()
            return session.scalars(sqlalchemy.select(User).where(
                (User.id >= from_id) & (User.id <= to_id)
            )).all()
        except OverflowError:
            raise OverflowError('Argument too big')

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
                permission=UserPermissions.DEFAULT
            )
            session.add(user)
            session.commit()
            user.set_password(password)
            return user
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            raise ValueError('Email or Nickname already used')

    @staticmethod
    def delete_user(user_id: int) -> None:
        '''Deletes user by given id'''
        user = User.get_user(user_id)
        if user is None:
            raise ValueError('User not found')
        session = api.db.get_session()
        session.delete(user)
        session.commit()

    @staticmethod
    def get_user_by_nickname(user_nickname: str):
        if not User.validate_nickname():
            raise ValueError('Invalid nickname')
        session = api.db.get_session
        return session.scalars(
            sqlalchemy.select(User
                              ).where(User.nickname == user_nickname)).all()[0]

    def update_user_settings(self, time_for_reading: int = None,
                             time_for_solving: int = None,
                             time_for_typing: int = None):
        '''change question_id and correct_answer of choosen answer'''
        if time_for_reading is not None:
            self.time_for_reading = time_for_reading
        if time_for_solving is not None:
            self.time_for_solving = time_for_solving
        if time_for_typing is not None:
            self.time_for_typing = time_for_typing
        session = api.db.get_session()
        session.add(self)
        session.commit()
        return self

    def check_for_admin(self):
        if self.permission == UserPermissions.ADMIN:
            return True
        return False

    def check_permissions(self, permission: str|UserPermissions) -> bool:
        '''Returns True if user has enough permissions'''
        perms = permission
        if type(permission) is UserPermissions:
            perms = user_permissions_to_string(permission)
        our_perms = user_permissions_to_string(self.permission)
        if our_perms == 'admin': return True
        if perms == 'default' and our_perms == 'default': return True
        return False
