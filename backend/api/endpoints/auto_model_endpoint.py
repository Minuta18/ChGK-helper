from . import api_endpoint
from . import errors
from api import models
import flask
import typing
import permissions
import auth

class AutoModelEndpoint(api_endpoint.BaseApiEndpoint, models.ModelInfo):
    '''Auto model endpoint
    
    Automatic endpoint which is used for operations which requires to use 
    existing model 

    TODO: we need to separate authorization logic somehow
    
    Attrs:
        disable_auth (bool): if True, auth will be disabled
        
        + and please see models.ModelInfo
    '''
    
    disable_auth: bool = False
    access_controller = permissions.AccessController()
    
    def _get_access_level(self, obj: typing.Any) -> permissions.AccessType:
        usr = auth.AuthUser.get_current_user()        
        return self.access_controller.get_access_level(obj, usr)
        
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
            model = self.model_controller.get_by_id(model_id)
            
            if not self.disable_auth:
                access = self._get_access_level(model)
                if access == permissions.AccessType.DISALLOW:
                    return errors.NotEnoughPermissionsError().make_error()
                
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': self._model_as_dict(model),
            }), 200
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            }), 404
                
    def put(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:                
            model, status = self.model_controller.get_by_id(model_id)

            if not self.disable_auth:
                access = self._get_access_level(model)
                if access == permissions.AccessType.DISALLOW or \
                    access == permissions.AccessType.ALLOW_VIEW:
                    return errors.NotEnoughPermissionsError().make_error()

            model.edit(
                **self._filter_kwargs(**(flask.request.json[self.model_name])))
            
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
            }), 400
            
    def delete(self, model_id: models.id_type, **kwargs) -> flask.Response:
        try:
            model, status = self.model_controller.get_by_id(model_id)
            
            if not self.disable_auth:
                access = self._get_access_level(model)
                if access == permissions.AccessType.DISALLOW or \
                    access == permissions.AccessType.ALLOW_VIEW:
                    return errors.NotEnoughPermissionsError().make_error()
            
            if status != permissions.UserStatus.CREATOR:
                return errors.NotEnoughPermissionsError().make_error()
            
            self.access_controller.delete_access_for_object(model)
            model.delete()
            
            return flask.jsonify({
                'error': False,
                f'{self.model_name}': self._model_as_dict(model),
            })
        except models.exc.ModelNotFound:
            return flask.jsonify({
                'error': True,
                'detail': self._model_not_found_error(model_id),
            }), 404
            