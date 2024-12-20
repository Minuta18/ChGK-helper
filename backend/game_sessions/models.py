import api.endpoints
import api.models
from sqlalchemy import orm
import sqlalchemy

class GameSession(api.models.BaseModel):
    '''Documentation'''

    __tablename__ = 'game_sessions'

    questions_order: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.dialects.postgresql.ARRAY(sqlalchemy.Integer)
    )