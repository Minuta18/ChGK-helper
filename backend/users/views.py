from users import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask

users_router = flask.Blueprint('users_urls', 'users')

@users_router.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    '''Gets user by an id.
    
    Returns user by given id (int). If user not found returns 404 error.
    
    Args:
        user_id(int): user\'s id
    '''
    
    user = models.User.get_user(user_id)
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id { user_id }',
        })
    return flask.jsonify({
        'error': False,
        'id': user_id,
        'email': user.email,
        'nickname': user.nickname,
    }), 200
    
@users_router.route('/', methods=['GET'])
def get_users():
    '''Gets multiple users.
    
    Gets multiple users from a specified page. Page is users 
    from n + 1 to n + page_size. 

    Args:
        page_size (:obj:`int`, optional): The number of users in one page. 
            Default value is 20.
        page (:obj:`int`, optional): Page. Default value is 1.
    '''

    page_size = flask.request.args.get('page_size', 20, type=int)
    page = flask.request.args.get('page', 1, type=int)

    return flask.jsonify({
        'error': False,
        'users': [{
            'id': user.id,
            'email': user.email,
            'nickname': user.nickname,
        } for user in models.User(
            from_id=((page - 1) * page_size + 1), to_id=(page * page_size)
        )],
    }), 200





