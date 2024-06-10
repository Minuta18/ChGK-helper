'''This module contains singleton class

This module contains only singleton class

Attributes:
    Singleton: class that implements a singleton design pattern
'''

class Singleton:
    '''Singleton

    This class implements a singleton design pattern. Source:
    https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-impleme
    nting-singleton-in-python.

    Attributes:
        _instance (object or None): Created instance
    '''

    _instance = None

    # TODO: remove arg1. Currently I'm not sure how to handle this
    def __new__(class_, arg1, *args, **kwargs):
        ''':obj:`object`: returns a new instance if it not already exist.
        Otherwise, returns created instance
        '''
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
