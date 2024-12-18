from users import models
from sqlalchemy import orm
import api.models
import api.endpoints
import permissions
import api
import flask
import auth
import typing

users_router = flask.Blueprint('users_urls', 'users')

class UsersService(api.endpoints.AutoModelEndpoint):
    '''UsersService
    
    Implements GET, PUT, DELETE methods in /api/v1/users
    '''

    model: type[api.models.BaseModel] = models.User
    model_name: str = 'User'
    model_controller: api.models.ModelController = models.UserController()
    
    visible_fields: list[str] = ['id', 'email', 'nickname', 'time_for_reading',
        'time_for_solving', 'time_for_typing']
    
class UsersStaticService(api.endpoints.AutoEndpoint):
    '''UsersStaticService
    
    Implements POST method for /api/v1/users
    '''
    
    model: type[api.models.BaseModel] = models.User
    model_name: str = 'User'
    model_controller: api.models.ModelController = models.UserController()
    
    visible_fields: list[str] = ['id', 'email', 'nickname', 'time_for_reading',
        'time_for_solving', 'time_for_typing']
    default_everyone_permission: permissions.AccessType = \
        permissions.AccessType.ALLOW_VIEW
    
    def post(self, **kwargs) -> flask.Response:
        try:
            user = self.model_controller.create(
                **(flask.request.json[self.model_name])
            )
            
            self.access_controller.create_access_for_object(
                user, user, 
                default_access_for_everyone=self.default_everyone_permission,
            )
        except api.models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err),
            }), 400
            
    @staticmethod
    def user_as_dict(user: models.User) -> dict[str, typing.Any]:
        model = {key: getattr(model, key, None) 
            for key in UsersStaticService.visible_fields} 
        model['access_object_id'] = model.__tablename__ + ':' + model.id
        return model

class UserAuthService(api.endpoints.BaseApiEndpoint):
    access_controller = permissions.AccessController()
    aut_user_controller = auth.AuthUser()
    
    def get(self, **kwargs):
        user = self.aut_user_controller.get_current_user()
        
        if user is None:
            return flask.jsonify({
                'error': True,
                'detail': 'Incorrect token'
            })
        else:
            return flask.jsonify({
                'error': False,
                'user': UsersStaticService.user_as_dict(user)
            })

users_router.add_url_rule(
    '/<int:model_id>', view_func=UsersService.as_view('users_service'),
    methods=['GET', 'PUT', 'DELETE', ],
)
   
users_router.add_url_rule(
    '/', view_func=UsersStaticService.as_view('users_static_service'),
    methods=['POST', ],
)

users_router.add_url_rule(
    '/self', view_func=UserAuthService.as_view('users_auth_service'),
    methods=['GET', ],
)
