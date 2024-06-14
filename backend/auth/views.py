from auth import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask
import secrets
import users

auth_router = flask.Blueprint('auth_urls', 'auth')

@auth_router.route('/login', methods=['POST'])
def create_token():
    '''Generates a token by nickname and password.

    Creates a token for a user by the user's nickname and password

    Args:
        user_nickname(str): user's nickname
        user_password(str): user's password
    '''
    
    user_nickname = flask.request.json.get('user_nickname', '')
    user_password = flask.request.json.get('user_password', '')

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
        'token': token,
    }), 200

@auth_router.route('/logout/<int:user_id>', methods=['DELETE'])
def delete_token(user_id: int):
    '''Deletes the user's token by given id.'''
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

@auth_router.route('/<str:token')
def get_user_by_token(token: str):
    '''Gets user by a given token.'''

    try:
        user = models.Token.get_user_by_token(token)
    except ValueError:
        return flask.jsonify({
            'error': True,
            'detail': 'Token not used for any user'
        }), 404

    return flask.jsonify({
        'error': False,
    }), 200
