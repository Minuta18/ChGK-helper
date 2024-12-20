from . import BaseModel, ModelController, id_type
import typing

class ModelInfo:
    model: type[BaseModel]
    model_name: str
    model_controller: ModelController
    
    visible_fields: list[str]
    
    def _model_as_dict(self, 
        model: BaseModel,
        exclude_keys: list[str] = [],
    ) -> dict:
        '''I've just pasted this method from AutoModelEndpoint. Isn't it code 
        duplicating, is it?
        Right? 
        '''
        
        def parse_key(key: str, val: typing.Any):
            # if key in list_fields:
                # res = list()
                # for model in val:
                #     res.append(self._model_as_dict(model))
            return val
        
        result = {key: getattr(model, key, None) 
            for key in self.visible_fields if key not in exclude_keys} 
        result['access_object_id'] = model.__tablename__ + ':' + model.id
        return result

    def _filter_kwargs(
        self, kwargs: dict[str, typing.Any],
        exclude_keys: list[str] = [],
    ) -> dict[str, typing.Any]:
        '''Returns only kwargs which are in self.visible_field'''
        
        filtered = dict()
        for key, val in kwargs:
            if key in self.visible_fields and key not in exclude_keys:
                filtered[key] = val
        return filtered

    def _model_not_found_error(self, model_id: id_type|None = None):
        '''Returns text of error if model not found'''
        
        if model_id is None:
            return f'{self.model_name.title()} not found'
        return f'{self.model_name.title()} with id={model_id} not found'
