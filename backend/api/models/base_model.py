from api import api_orm
from sqlalchemy import orm
import sqlalchemy
import datetime
import typing_extensions

class BaseModel(api_orm.orm_base):
    '''Model interface'''

    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True,
    )
    
    time_created: orm.Mapped[datetime.datetime] = orm.mapped_column(
        sqlalchemy.DateTime(timezone=True), 
        server_default=sqlalchemy.func.now()
    )
    
    time_updated: orm.Mapped[datetime.datetime] = orm.mapped_column(
        sqlalchemy.DateTime(timezone=True),
        onupdate=sqlalchemy.func.now()
    )
    
    def edit(self, **kwargs) -> None:
        pass
    
    def delete(self) -> typing_extensions.Self:
        return self
