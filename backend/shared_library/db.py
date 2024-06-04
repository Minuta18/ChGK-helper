# -*- coding: utf-8 -*-
'''DB connection module

This module contains classes and functions that are used to establish 
connection to SQL database (any that supports SQLalchemy).

Attributes:
    DB_connection: Object that represents the database connection

TODO:
    * implement asynchronous version of DB_connection
'''

import sqlalchemy
from sqlalchemy.ext import declarative
from sqlalchemy import orm
import typing

class DB_connection:
    '''Object that represents the database connection
    
    '''