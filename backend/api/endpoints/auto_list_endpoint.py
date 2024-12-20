from . import errors
from .api_endpoint import BaseApiEndpoint
from .auto_model_endpoint import AutoModelEndpoint
from api import models
import permissions
import typing
import flask
import auth

class AutoListEndpoint(AutoModelEndpoint):
    '''Auto list endpoint
    
    Sometimes you need to display a list of something. Here it is
    '''
    
    disable_auth: bool = False
    access_controller = permissions.AccessController()
    list_field: str
    list_field_name: str = 'items'
    
    def __init__(self):
        assert isinstance(self.model, models.ListModel), \
            'Model must be ListModel'
    
    def _get_access_level(self, obj: typing.Any) -> permissions.AccessType:
        usr = auth.AuthUser.get_current_user()        
        return self.access_controller.get_access_level(obj, usr)
    
    def _make_validation_error(self, error: models.exc.ValidationError) -> str:
        '''Same as self._model_not_found_error()'''
        if len(error.args) < 1:
            return 'No detail provided'
        return str(error)
    
    def _get_dict(
        self, model: typing.Any, items: typing.Any
    ) -> dict[str, typing.Any]:
        response = self._model_as_dict(
            model, exclude_keys=[self.list_field, ])
        response[self.list_field_name] = [
            self._model_as_dict(item.child) for item in items]
        return response
    
    def get(self, model_id: models.id_type, **kwargs) -> flask.Response:
        '''Returns model and list of its items
        Supports `?limit=<int>`, 
        `?sort_by=[time_updated, time_created, id, ...]`, `?reverse=<bool>`,
        `?page=<int>`, 
        '''
        
        try:                
            model, status = self.model_controller.get_by_id(model_id)
            items = model.get_items(**kwargs)
            
            if not self.disable_auth:
                access = self._get_access_level(model)
                if access == permissions.AccessType.DISALLOW:
                    return errors.NotEnoughPermissionsError().make_error()
                    
            return flask.jsonify(self._get_dict(model, items)), 200
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            })
            
    def put(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:
            model, status = self.model_controller.get_by_id(model_id)
            
            if not self.disable_auth:
                access = self._get_access_level(model)
                if access == permissions.AccessType.DISALLOW:
                    return errors.NotEnoughPermissionsError().make_error()
            
            model.edit(**self._filter_kwargs(
                flask.request.json.get[self.model_name],
                [self.list_field_name, ],
            ))
            items = model.get_items(**kwargs)
            
            return flask.jsonify(self._get_dict(model, items)), 200
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            })
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
            
class ListManagerEndpoint(BaseApiEndpoint, models.ModelInfo):
    '''Auto list endpoint
    
    Sometimes you need to display a list of something. Here it is
    '''
    
    disable_auth: bool = False
    access_controller = permissions.AccessController()
    list_field: str
    list_field_name: str = 'items'
    
    def get(self, 
        model_id: models.id_type, item_order_id: models.id_type
    ) -> flask.Response:
        
