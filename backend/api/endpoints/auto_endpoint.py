from . import api_endpoint
from api import models
import flask

class AutoEndpoint(api_endpoint.BaseApiEndpoint):
    '''Auto endpoint
    
    API endpoint that generates responses automatically 
    '''

    model: type[models.BaseModel]
    model_name: str
    model_controller: models.ModelController
    
    visible_fields: list[str]
    
    def get(self, model_id, **kwargs) -> flask.Response:
        try:
            model = self.model_controller.get_by_id()
                
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': {key: getattr(model, key, None) 
                    for key in self.visible_fields} 
            }), 200
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': (
                    f'{self.model_name.title()} with id={model_id} not found'
                )
            }), 404
