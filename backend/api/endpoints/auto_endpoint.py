from . import api_endpoint
from api import models
import flask
import typing

class AutoEndpoint(api_endpoint.BaseApiEndpoint):
    '''Auto endpoint
    
    API endpoint that generates responses automatically 
    '''

    model: type[models.BaseModel]
    model_name: str
    model_controller: models.ModelController
    
    visible_fields: list[str]
    
    def _model_as_dict(self, model: models.BaseModel) -> dict:
        return {key: getattr(model, key, None) 
            for key in self.visible_fields} 
        
    def _model_not_found_error(self, model_id: models.id_type|None = None):
        if model_id is None:
            return f'{self.model_name.title()} not found'
        return f'{self.model_name.title()} with id={model_id} not found'

    def _filter_kwargs(
        self, kwargs: dict[str, typing.Any]
    ) -> dict[str, typing.Any]:
        filtered = dict()
        for key, val in flask.request.json:
            if key in self.visible_fields:
                filtered[key] = val
        return filtered
    
    def get(self, model_id, **kwargs) -> flask.Response:
        try:
            model = self.model_controller.get_by_id()
                
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': self._model_as_dict(model),
            }), 200
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            }), 404
    
    def post(self, model_id: models.id_type, **kwargs) -> flask.Response:
        pass
            
    def patch(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:            
            model = self.model_controller.edit_by_id(
                model_id,
                **self._filter_kwargs(**kwargs) 
            )
            
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': self._model_as_dict(model),
            })
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            }), 404
        except models.exc.ValidationError as err:
            if len(err.args) < 1:
                return flask.jsonify({
                    'error': True,
                    'detail': 'No detail provided'
                })
            return flask.jsonify({
                'error': True,
                'detail': err.args[0]
            })
