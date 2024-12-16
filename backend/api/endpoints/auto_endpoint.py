from . import api_endpoint
from . import errors
from api import models
import auth
import flask

class AutoEndpoint(api_endpoint.BaseApiEndpoint, models.ModelInfo):
    '''Auto endpoint
    
    Automatic endpoint which is used for operations which does not require to 
    use existing model 
    
    literally same with auto_model_endpoint so visit it please 
    (than go to jail)
    '''
    
    disable_auth: bool = False
    
    login_required: list
    
    def _is_user_unauthorized(self, method: str) -> bool:
        if method in self.login_required:
            return auth.AuthUser.get_current_user() is None
        return False
    
    def get(self, *args, **kwargs) -> flask.Response:
        if self._is_user_unauthorized('get'):
            return errors.UnauthorizedError().make_error() 
        return super().get(*args, **kwargs)
    
    def post(self, **kwargs) -> flask.Response:
        try:
            if self._is_user_unauthorized('post'):
                return errors.UnauthorizedError().make_error() 
            
            self.model_controller.create(
                **(flask.request.json[self.model_name]))
        except models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err)
            })

    def put(self, *args, **kwargs) -> flask.Response:
        if self._is_user_unauthorized('put'):
            return errors.UnauthorizedError().make_error() 
        return super().put(*args, **kwargs)
    
    def patch(self, *args, **kwargs) -> flask.Response:
        if self._is_user_unauthorized('patch'):
            return errors.UnauthorizedError().make_error() 
        return super().patch(*args, **kwargs)
    
    def delete(self, *args, **kwargs) -> flask.Response:
        if self._is_user_unauthorized('delete'):
            return errors.UnauthorizedError().make_error() 
        return super().delete(*args, **kwargs)
