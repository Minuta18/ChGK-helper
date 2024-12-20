from . import api_endpoint
from api import models
import permissions
import flask

class AutoListEndpoint(api_endpoint.BaseApiEndpoint, models.ModelInfo):
    '''Auto list endpoint
    
    Sometimes you need to display a list of something. Here it is
    '''
    
    disable_auth: bool = False
    access_controller = permissions.AccessController()
    list_field: str
    
    def get(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:
            ...
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            })
    