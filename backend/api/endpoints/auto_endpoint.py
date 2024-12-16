from . import api_endpoint
from api import models
from permissions import
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
    
    def post(self, **kwargs) -> flask.Response:
        try:
            if 'post' in self.login_required:
                pass
            
            self.model_controller.create(
                **(flask.request.json[self.model_name]))
        except models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err)
            })


