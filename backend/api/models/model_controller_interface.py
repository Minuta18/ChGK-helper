import typing

class IModelController:
    '''Model interface
    
    Interface that specifies required methods for model. More specifically:
     - get_by_id(id: int): returns model by id
     - edit_by_id(id: int, **kwargs: Any): finds model by id and edits it
     - delete_by_id(id: int): returns model by id
     - create(**kwargs: Any): creates model 
    '''
    
    def get_by_id(id: int) -> typing.Any:
        '''Returns model by id
        
        Returns model by id. Raises `ModelNotFound` if there is no such model
        
        Args:
            id (int): id of model to find
            
        Raises:
            ModelNotFound: raises `ModelNotFound` if there is no such model
            
        Returns:
            Any: found model
        '''
        
        raise NotImplementedError
    
    def edit_by_id(id: int, **kwargs: typing.Any) -> typing.Any:
        '''Edits model by id
        
        Finds model by id and then edits it using kwargs (keys=new_value). 
        Returns edited model
        
        Args:
            id (int): id of model to find
            
        Raises:
            ModelNotFound: raises `ModelNotFound` if there is no such model
            
        Returns:
            Any: found model
        '''
        return NotImplementedError
    
    def delete_by_id(id: int) -> typing.Any:
        '''Deletes model by id
        
        Deletes model by id. Raises `ModelNotFound` if there is no such model
        
        Args:
            id (int): id of model to find
            
        Raises:
            ModelNotFound: raises `ModelNotFound` if there is no such model
            
        Returns:
            Any: deleted model
        '''
        return NotImplementedError
    
    def create(**kwargs: typing.Any) -> typing.Any:
        '''Creates new model
        
        Create new model and returns it
        
        Args:
            **kwargs: keys in format key=value
           
        Returns:
            Any: created models
        '''
        return NotImplementedError
