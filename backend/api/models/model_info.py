from . import BaseModel, ModelController

class ModelInfo:
    model: type[BaseModel]
    model_name: str
    model_controller: ModelController
    
    visible_fields: list[str]
    
    def _model_as_dict(self, model: BaseModel) -> dict:
        '''I've just pasted this method from AutoModelEndpoint. Isn't it code 
        duplicating, is it?
        Right? 
        '''
        
        result = {key: getattr(model, key, None) 
            for key in self.visible_fields} 
        result['access_object_id'] = model.__tablename__ + ':' + model.id
