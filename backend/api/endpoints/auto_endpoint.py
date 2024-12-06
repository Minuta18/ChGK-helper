from . import api_endpoint
from api import models
import flask

class AutoEndpoint(api_endpoint.BaseApiEndpoint, models.ModelInfo):
    '''Auto endpoint
    
    Automatic endpoint which is used for operations which does not require to 
    use existing model 
    '''
    
    def post(self, **kwargs) -> flask.Response:
        try:
            self.model_controller.create(
                **(flask.request.json[self.model_name]))
        except models.exc.ValidationError as err:
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err)
            })


