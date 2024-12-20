from . import BaseModel, id_type
from sqlalchemy import orm
import sqlalchemy
import typing

class BaseAssociation(BaseModel):
    '''Base association 
    
    Base class used for association objects
    '''
    
    __abstract__ = True
    
    parent_id: orm.Mapped[id_type] = ...
    child_id: orm.Mapped[id_type] = ...
    order_marker: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False,
    )
    child: typing.Any
    parent: typing.Any

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
    