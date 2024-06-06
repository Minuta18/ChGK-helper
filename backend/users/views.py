from users import models
from sqlalchemy import orm
import sqlalchemy
import api
import flask

users_router = flask.Blueprint('users_urls', 'users')

@users_router.route('/<int:user_id>')
def get_user(user_id: int):
    '''Gets user by an id.
    
    Returns user by given id (int). If user not found returns 404 error.
    
    Args:
        user_id(int): user\'s id
    '''
    
    session = api.db.get_session()
    user = session.get(models.User, user_id)
    if user is None:
        flask.abort(404)
    return flask.jsonify({
        'id': user_id,
        'email': user.email,
        'nickname': user.nickname,
    }), 200
    