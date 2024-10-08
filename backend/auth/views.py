from auth import models
from sqlalchemy import orm
import flask
import users
import auth

auth_router = flask.Blueprint('auth_urls', 'auth')

@auth_router.route('/login', methods=['POST'])
def create_token():
    '''Generates a token by nickname and password.

    Creates a token for a user by the user's nickname and password

    Args:
        nickname(str): user's nickname
        password(str): user's password
    '''
    
    user_nickname = flask.request.json.get('nickname', '')
    user_password = flask.request.json.get('password', '')

    user = users.models.User.get_user_by_nickname(user_nickname)
    if user is None:
        return flask.jsonify({
            'errors': True,
            'detail': 'Could not find user',
        }), 404

    if not user.verify_password(user_password):
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect password',
        }), 401

    token = models.Token.create_token(user.id)
    return flask.jsonify({
        'error': False,
        'token': token.token,
    }), 200

@auth_router.route('/logout/<int:user_id>', methods=['DELETE'])
def delete_tokens(user_id: int):
    '''Deletes the users' token by given id.'''
    try:
        models.Token.delete_token(user_id)
        return flask.jsonify({
            'error': False
        }), 200
    except ValueError:
        return flask.jsonify({
            'error': True,
            'detail': 'User not found',
        }), 404
    except OverflowError:
        return flask.jsonify({
            'error': True,
            'detail': 'User not found',
        }), 404
    
@auth_router.route('/check', methods=['GET', ])
def check_token():
    token = flask.request.headers.get('Authorization', '')
    user = auth.models.Token.get_user_by_token(token.removeprefix('Bearer '))
    if user is None:
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect token',
        }), 401
    else:
        return flask.jsonify({
            'error': False,
            'detail': 'Token is valid',
        }), 200
