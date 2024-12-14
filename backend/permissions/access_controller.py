from . import access_type
from . import access
from api import models
from api import db
from users import models as user_models
import sqlalchemy

class AccessController:
    '''AccessController
    
    Finds access level by given user 
    
    !!!HOLY FUCKING SHIT!!! 
    IS THAT A MOTHERFUCKING TNO REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!
    '''
    
    @staticmethod
    def get_access_level(
        object: models.BaseModel, 
        user: user_models.User | None = None,
    ) -> access_type.AccessType:
        session = db.get_session()
        access_objects = session.scalars(
            sqlalchemy.select(access.Access).where(
                (access.Access.model_id == object.id) &
                (access.Access.model_name == object.__tablename__)
            )
        ).all()
        
        everyone_access, special_access = None, None
        for obj in access_objects:
            if obj.acc_type == access_type.AccessSelector.EVERYBODY:
                everyone_access = obj
            elif obj.acc_type == access_type.AccessSelector.SPECIAL:
                special_access = obj

        if special_access is not None:
            return special_access.acc_type
        
        if everyone_access is not None:
            return everyone_access.acc_type
        
        return access_type.AccessType.DISALLOW
