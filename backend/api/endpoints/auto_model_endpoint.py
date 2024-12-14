from . import api_endpoint
from api import models
import flask
import typing

class AutoModelEndpoint(api_endpoint.BaseApiEndpoint, models.ModelInfo):
    '''Auto model endpoint
    
    Automatic endpoint which is used for operations which requires to use 
    existing model 
    
    TODO: we need to separate authorization logic somehow
    '''
    
    def _model_as_dict(self, model: models.BaseModel) -> dict:
        '''Represents model as dict
        
        Represents model as dicts, where keys equals keys from model and blah 
        blah blah im too tired to write this comment
        '''
        
        return {key: getattr(model, key, None) 
            for key in self.visible_fields} 
        
    def _model_not_found_error(self, model_id: models.id_type|None = None):
        '''Returns text of error if model not found'''
        
        if model_id is None:
            return f'{self.model_name.title()} not found'
        return f'{self.model_name.title()} with id={model_id} not found'

    def _make_validation_error(self, error: models.exc.ValidationError) -> str:
        '''Same as self._model_not_found_error()'''
        if len(error.args) < 1:
            return 'No detail provided'
        return str(error)

    def _filter_kwargs(
        self, kwargs: dict[str, typing.Any]
    ) -> dict[str, typing.Any]:
        '''Returns only kwargs which are in self.visible_field'''
        
        filtered = dict()
        for key, val in kwargs:
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
                
    def patch(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:            
            model = self.model_controller.edit_by_id(
                model_id,
                **self._filter_kwargs(**(flask.request.json[self.model_name])) 
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
            return flask.jsonify({
                'error': True,
                'detail': self._make_validation_error(err)
            })
            
    def delete(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:
            model = self.model_controller.delete_by_id(model_id)
            
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': self._model_as_dict(model),
            })
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            }), 404
