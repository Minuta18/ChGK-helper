from users import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask
import auth

users_router = flask.Blueprint('users_urls', 'users')

@users_router.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    '''Gets user by an id.

    Returns user by given id (int). If user not found returns 404 error.

    Args:
        user_id(int): user\'s id
    '''

    try:
        user = models.User.get_user(user_id)
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404
    return flask.jsonify({
        'error': False,
        'user': {
            'id': user_id,
            'email': user.email,
            'nickname': user.nickname,
        }
    }), 200

@users_router.route('/', methods=['GET'])
def get_users():
    '''Gets multiple users.

    Gets multiple users from a specified page. Page is users
    from n + 1 to n + page_size

    Args:
        page_size (:obj:`int`, optional): The number of users in one page.
            Default value is 20.
        page (:obj:`int`, optional): Page. Default value is 1.
    '''

    page_size = flask.request.args.get('page_size', 20, type=int)

    if (page_size < 1 or page_size > 100):
        return flask.jsonify({
            'error': True,
            'detail': f'Invalid page size: {page_size}'
        }), 400

    page = flask.request.args.get('page', 1, type=int)

    if (page < 1):
        return flask.jsonify({
            'error': True,
            'detail': f'Invalid page: {page}',
        }), 400

    try:
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
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': 'Arguments too big'
        })

@users_router.route('/', methods=['POST'])
def create_user():
    '''Creates new user.

    Creates new user.

    Args:
        email (str): Email of the new user
        nickname (str): Nickname of the new user.
        password (str): Password of the new user.
    '''

    if flask.request.headers.get('Content-Type') != 'application/json':
        return flask.jsonify({
            'error': True,
            'message': 'Incorrect Content-Type header',
        }), 400
    email = flask.request.json.get('email', '')
    nickname = flask.request.json.get('nickname', '')
    password = flask.request.json.get('password', '')

    try:
        user = models.User.create_user(email, nickname, password)
    except ValueError as e:
        return flask.jsonify({
            'error': True,
            'message': repr(e),
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
        
    user = auth.verify_token(flask.request.headers.get('Authorization', ''))
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect token'
        }), 401
    elif user.id != user_id:
        return flask.jsonify({
            'error': True,
            'detail': 'Access denied'
        }), 401

    password = flask.request.json.get('old_password', '')
    new_password = flask.request.json.get('new_password', '')

    try:
        user = models.User.get_user(user_id)
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404

    if user is None:
        return flask.jsonify({
            'error': True,
            'message': 'User not found',
        }), 404

    # print(password, user.hashed_password, user.verify_password(password))
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

@users_router.route('/<int:user_id>', methods=['PUT'])
def edit_user_settings(user_id: int):
    '''Edits user by given id.

    Edits user by given id.

    Args:
        email (:obj:`str`, optional): New email of the user.
        nickname (:obj:`str`, optional): New nickname of the new user.
    '''

    user = auth.verify_token(flask.request.headers.get('Authorization', ''))
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect token'
        }), 401
    elif user.id != user_id:
        return flask.jsonify({
            'error': True,
            'detail': 'Access denied'
        }), 401

    email = flask.request.args.get('email', None, type=str)
    nickname = flask.request.args.get('nickname', None, type=str)

    print(email)

    try:
        user = models.User.get_user(user_id)
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404

    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'User not found'
        }), 404

    if email is not None:
        if not models.User.validate_email(email):
            return flask.jsonify({
                'error': True,
                'detail': 'Email is invalid',
            }), 400

        user.email = email

    if nickname is not None:
        if not models.User.validate_nickname(nickname):
            return flask.jsonify({
                'error': True,
                'detail': 'Nickname is invalid',
            }), 400

        user.nickname = nickname

    session = api.db.get_session()
    session.add(user)
    try:
        session.commit()
        return flask.jsonify({
            'error': False,
            'id': user.id,
            'email': user.email,
            'nickname': user.nickname,
        }), 200
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        return flask.jsonify({
            'error': True,
            'detail': 'email already exists',
        }), 400

@users_router.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    '''Deletes user by given id'''

    user = auth.verify_token(flask.request.headers.get('Authorization', ''))
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect token'
        }), 401
    elif user.id != user_id:
        return flask.jsonify({
            'error': True,
            'detail': 'Access denied'
        }), 401

    try:
        models.User.delete_user(user_id)
        return flask.jsonify({
            'error': False,
        }), 200
    except ValueError:
        return flask.jsonify({
            'error': True,
            'detail': 'User not found',
        }), 404
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404

@users_router.route('/<int:user_id>', methods=['GET'])
def get_time_settings(user_id: int):
    '''Gets time settings by an id.

    Returns 3 time settings by given id (int).
    If user not found returns 404 error.

    Args:
        user_id(int): user\'s id
    '''
    if auth.verify_token(auth.auth.current_user()).id != user_id:
        return flask.jsonify({
            'error': True,
            'detail': 'Can\'t view data of another user'
        }), 401

    try:
        user = models.User.get_user(user_id)
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404
    return flask.jsonify({
        'error': False,
        'user': {
            'time_for_reading': user.time_for_reading,
            'time_for_solving': user.time_for_solving,
            'time_for_typing': user.time_for_typing,
        }
    }), 200

@users_router.route('/settings/<int:user_id>', methods=['PUT'])
def edit_user_sttings(user_id: int):
    '''Edits user settings by given id.

    Edits user by given id.

    Args:
        time_for_reading (:obj:`int`, optional):
        New time for reading setting of the user.
        time_for_solving (:obj:`int`, optional):
        New time for solving setting of the user.
        time_for_typing (:obj:`int`, optional):
        New time for typing setting of the user.
    '''
    
    if auth.verify_token(auth.auth.current_user()).id != user_id:
        return flask.jsonify({
            'error': True,
            'detail': 'Can\'t edit data of another user'
        }), 401

    user = auth.verify_token(flask.request.headers.get('Authorization', ''))
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect token'
        }), 401
    elif user.id != user_id:
        return flask.jsonify({
            'error': True,
            'detail': 'Access denied'
        }), 401

    time_for_reading = flask.request.args.get('time_for_reading',
                                              None, type=int)
    time_for_solving = flask.request.args.get('time_for_solving',
                                              None, type=int)
    time_for_typing = flask.request.args.get('time_for_typing',
                                             None, type=int)

    try:
        user = models.User.get_user(user_id)
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}',
        }), 404

    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': f'Could not find user with id {user_id}'
        }), 404

    user.update_user_settings(time_for_reading,
                              time_for_solving,
                              time_for_typing)
    return flask.jsonify({
        'error': False,
        'time_for_reading': user.time_for_reading,
        'time_for_solving': user.time_for_solving,
        'time_for_typing': user.time_for_typing,
    }), 200
