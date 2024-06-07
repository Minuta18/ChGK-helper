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
        }), 404
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

    if (page_size < 1 or page_size > 100):
        return flask.jsonify({
            'error': True,
            'detail': f'Incorrect page size: { page_size }'
        })
    
    page = flask.request.args.get('page', 1, type=int)

    return flask.jsonify({
        'error': False,
        'users': [{
            'id': user.id,
            'email': user.email,
            'nickname': user.nickname,
        } for user in models.User.get_users(
            from_id=((page - 1) * page_size + 1), to_id=(page * page_size)
        )],
    }), 200

@users_router.route('/', methods=['POST'])
def create_user():
    '''Creates new user.
    
    Creates new user.

    Args:
        email (str): Email of the new user. 
        nickname (str): Nickname of the new user.
        password (str): Password of the new user.
    '''
    
    if flask.request.headers.get('Content-Type') != 'application/json':
        return flask.jsonify({
            'error': True,
            'message': 'Incorrect Content-Type header',
        })
    email = flask.request.json.get('email', '')
    nickname = flask.request.json.get('nickname', '')
    password = flask.request.json.get('password', '')
    
    try:
        user = models.User.create_user(email, nickname, password)
    except ValueError as e:
        return flask.jsonify({
            'error': True,
            'message': e.message,
        }), 400
        
    return flask.jsonify({
        'error': False,
        'id': user.id,
        'email': user.email,
        'nickname': user.nickname,    
    }), 201
    
@users_router.route('/<int:user_id>/change_password', methods=['PUT'])
def change_password(user_id: int):
    '''Changes password of a user by an id.
    
    Changes password of a user by an id. Needs old password.

    Args:
        old_password (str): Old password. 
        new_password (str): New password.
    '''
    
    if flask.request.headers.get('Content-Type') != 'application/json':
        return flask.jsonify({
            'error': True,
            'message': 'Incorrect Content-Type header',
        })
        
    password = flask.request.headers.get('old_password', '')
    new_password = flask.request.headers.get('new_password', '')
               
    user = models.User.get_user(user_id)
    if user is None:
        return flask.jsonify({
            'error': True,
            'message': 'User not found',
        }), 404
        
    if not user.verify_password(password):
        return flask.jsonify({
            'error': True,
            'message': 'Password is incorrect',
        }), 401
        
    if not models.User.validate_password(new_password):
        return flask.jsonify({
            'error': True,
            'message': 'Invalid password',
        }), 400
  
    user.set_password(new_password)
        
    return flask.jsonify({
        'error': False,
    }), 200


