import typing
import abc
from .types import id_type

class ModelController(abc.ABC):
    '''Model interface
    
    Interface that specifies required methods for model. More specifically:
     - get_by_id(id: int): returns model by id
     - edit_by_id(id: int, **kwargs: Any): finds model by id and edits it
     - delete_by_id(id: int): returns model by id
     - create(**kwargs: Any): creates model 
    '''
    
    def get_by_id(id: id_type) -> typing.Any:
        '''Returns model by id
        
        Returns model by id. Raises `ModelNotFound` if there is no such model
        
        Args:
            id (id_type): id of model to find
            
        Raises:
            ModelNotFound: raises `ModelNotFound` if there is no such model
            
        Returns:
            Any: found model
        '''
        
        raise NotImplementedError
    
    def create(**kwargs: typing.Any) -> typing.Any:
        '''Creates new model
        
        Create new model and returns it
        
        Args:
            **kwargs: keys in format key=value
           
        Returns:
            Any: created models
        '''
        
        raise NotImplementedError
