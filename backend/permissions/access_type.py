import enum

class AccessType(enum.Enum):
    ALLOW_EDIT = 'ALLOW_EDIT',
    ALLOW_VIEW = 'ALLOW_VIEW',
    DISALLOW = 'DISALLOW',

class AccessSelector(enum.Enum):
    EVERYBODY = 'EVERYBODY',
    UNAUTHENTICATED = 'UNAUTHENTICATED',
    SPECIAL = 'SPECIAL'
