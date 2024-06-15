from auth import models
import users
import flask
import functools

def verify_token(token: models.Token) -> users.models.User:
    '''Returns user by given token'''
    user = models.Token.get_user_by_token(token)
    return user

def login_required(role: str='user'):
    def decorator(func):
        '''Checks if user is logged in

        Returns 401 if user is not logged in or if user has not enough 
        permissions.
        '''
        
        @functools.wraps(func)
        def decorated_func(*args, **kwargs):
            token = flask.request.headers.get('Authorization', '')
            user = verify_token(token)
            if user is None:
                return flask.jsonify({
                    'error': True,
                    'detail': 'Incorrect token',
                }), 401
            if not user.check_permissions(role):
                return flask.jsonify({
                    'error': True,
                    'detail': 'Permission denied',
                }), 401
            return func(*args, **kwargs)
        return decorated_func
    return decorator
