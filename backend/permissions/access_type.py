import enum

class AccessType(enum.Enum):
    ALLOW_EDIT = 'ALLOW_EDIT',
    ALLOW_VIEW = 'ALLOW_VIEW',
    ALLOW_RECOMMENDING = 'ALLOW_RECOMMENDING' # Option for the future, it can 
        # be used in recommendation system 
    DISALLOW = 'DISALLOW',

class AccessSelector(enum.Enum):
    EVERYBODY = 'EVERYBODY',
    SPECIAL = 'SPECIAL',

class UserStatus(enum.Enum):
    DEFAULT = 'DEFAULT',
    ADMIN = 'ADMIN',
    CREATOR = 'CREATOR',
