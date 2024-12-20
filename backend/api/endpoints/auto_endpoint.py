from . import api_endpoint
from . import errors
from api import models
import auth
import flask
import permissions

class AutoEndpoint(api_endpoint.BaseApiEndpoint, models.ModelInfo):
    '''Auto endpoint
    
    Automatic endpoint which is used for operations which does not require to 
    use existing model 
    
    literally same with auto_model_endpoint so visit it please 
    (than go to jail)
    '''
    
    disable_auth: bool = False
    access_controller = permissions.AccessController()
    default_everyone_permission: permissions.AccessType = \
        permissions.AccessType.DISALLOW

    def _is_user_unauthorized(self, method: str) -> bool:
        if method in self.login_required:
            return auth.AuthUser.get_current_user() is None
        return False
    
    def post(self, **kwargs) -> flask.Response:
        try:
            if self._is_user_unauthorized('post'):
                return errors.UnauthorizedError().make_error() 
            
            model = self.model_controller.create(
                **(flask.request.json[self.model_name]))
            
            self.access_controller.create_access_for_object(
                model, auth.AuthUser.get_current_user(), 
                default_access_for_everyone=self.default_everyone_permission,
            )
            
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': self._model_as_dict(model),
            }), 201
        except models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err)
            }), 400
        except models.exc.IndexError as err:
            return flask.jsonify({
                'error': True,
                'detail': str(err),
            }), 400
