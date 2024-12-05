from . import BaseModel, ModelController

class ModelInfo:
    model: type[BaseModel]
    model_name: str
    model_controller: ModelController
    
    visible_fields: list[str]
