import flask
import users
from . import models

class AuthUser:
    '''AuthUser class
    
    Class to manage user using tokens
    '''
    
    @staticmethod
    def get_user_by_token(token: str) -> users.models.User | None:
        token = models.Token.find_token(token)
        return token.get_user(token)
    
    @staticmethod
    def get_current_user() -> users.models.User | None:
        token = flask.request.headers.get('Authorization')
        return AuthUser.get_user_by_token(token)
        