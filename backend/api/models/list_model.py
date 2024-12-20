from . import BaseModel
import typing

class ListModel(BaseModel):
    '''List model
    
    Model which contains a list of other models
    '''
    
    __abstract__ = True 
    
    def get_items(self, 
        limit: int = 20,
        sort_by: str = 'time_updated',
        reverse: bool = False,
        page: int = 1,
    ) -> list[typing.Any]:
        pass
    