from auth import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask
import secrets
import users

auth_router = flask.Blueprint('auth_urls', 'auth')

@auth_router.route('/login', methods=['POST'])
def create_token(user_nickname: str, user_password: str):
    '''Generates a token by nickname and password.

    Creates a token for a user by the user's nickname and password

    Args:
        user_nickname(str): user's nickname
        user_password(str): user's password
    '''

    user = users.models.User.get_user_by_nickname(user_nickname)
    
    if not users.models.User.verify_password(user, user.hashed_password, 'bcrypt'):
        flask.jsonify({
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

