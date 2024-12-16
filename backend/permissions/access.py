from sqlalchemy import orm
import sqlalchemy
import api
import api.models
from . import access_type

MAX_TABLENAME_LENGTH = 24

class Access(api.models.BaseModel):
    '''Access model
    
    Model to store objects accesses
    '''
    
    __tablename__ = 'access'

    selector: orm.Mapped[access_type.AccessSelector] = orm.mapped_column(
        nullable=False,
    )
    special_user_id: orm.Mapped[api.models.id_type] = orm.mapped_column(
        nullable=True,
    ),
    special_user_status: orm.Mapped[access_type.UserStatus] = \
        orm.mapped_column(nullable=True)
    acc_type: orm.Mapped[access_type.AccessType] = orm.mapped_column(
        nullable=False
    )
    model_id: orm.Mapped[int] = orm.mapped_column(
        nullable=False
    )
    model_name: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.String(MAX_TABLENAME_LENGTH), nullable=False
    )
