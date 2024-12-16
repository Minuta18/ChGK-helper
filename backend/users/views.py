from users import models
from sqlalchemy import orm
import api.models
import api.endpoints
import sqlalchemy
import api
import flask
import auth

users_router = flask.Blueprint('users_urls', 'users')

class UsersService(api.endpoints.AutoModelEndpoint):
    model: type[api.models.BaseModel] = models.User
    model_name: str = 'User'
    model_controller: api.models.ModelController = models.UserController()
    
    visible_fields: list[str] = ['id', 'email', 'nickname', 'time_for_reading',
        'time_for_solving', 'time_for_typing']
    
users_router.add_url_rule(
    '/<int:model_id>', 
    view_func=UsersService.as_view('users_service')
)

@users_router.route('/self', methods=['GET', ])
def get_user_by_token():
    token = flask.request.headers.get('Authorization', '')
    user = auth.models.Token.get_user_by_token(token.removeprefix('Bearer '))
    if user is None:
        # print(token, token.removeprefix('Bearer '), sep='\n')
        return flask.jsonify({
            'error': True,
            'detail': 'Incorrect token',
        }), 401
    else:
        return flask.jsonify({
            'error': False,
            'id': user.id,
            'email': user.email,
            'nickname': user.nickname,
        }), 200

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
        
    user = auth.verify_token(
        flask.request.headers.get('Authorization', '').removeprefix('Bearer ')
    )
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
