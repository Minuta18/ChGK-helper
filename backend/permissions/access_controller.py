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
    
    # def why(self): return 'Yo, Speer!'
    
    def get_access_level(self,
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
            if user is not None:
                if obj.acc_type == access_type.AccessSelector.SPECIAL and \
                    obj.special_user_id == user.id:
                    special_access = obj

        if special_access is not None:
            return special_access.acc_type, special_access.special_user_status
        
        if everyone_access is not None:
            return everyone_access.acc_type, access_type.UserStatus.DEFAULT
        
        return access_type.AccessType.DISALLOW, access_type.UserStatus.DEFAULT
    
    def create_access_for_object(self, 
        object: models.BaseModel, 
        user: user_models.User,
        default_access_for_everyone: access_type.AccessType =  
            access_type.AccessType.DISALLOW,
        default_access_for_creator: access_type.AccessType =
            access_type.AccessType.ALLOW_EDIT
    ) -> None:
        '''Creates access instances for object'''
        
        session = db.get_session()
        
        everybody_access = access.Access(
            selector=access_type.AccessSelector.EVERYBODY,
            acc_type=default_access_for_everyone,
            model_id=object.id,
            model_name=object.__tablename__,
        )
        
        special_access = access.Access(
            selector=access_type.AccessSelector.SPECIAL,
            acc_type=default_access_for_creator,
            special_user_id=user.id,
            special_user_status=access_type.UserStatus.CREATOR,
            model_id=object.id,
            model_name=object.__tablename__
        )
        
        session.add(everybody_access)
        session.add(special_access)
        session.commit()
        
    def delete_access_for_object(self,
        object: models.BaseModel, 
    ) -> None:
        '''Deletes access instances for object'''

        session = db.get_session()
        
        access_objects = session.scalars(
            sqlalchemy.select(access.Access).where(
                (access.Access.model_id == object.id) &
                (access.Access.model_name == object.__tablename__)
            )
        ).all()
        
        for obj in access_objects:
            session.delete(obj)
