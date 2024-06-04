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
from sqlalchemy import orm
from shared_library import utils
import typing

class DB_connection(utils.singleton):
    '''Object that represents the database connection'''

    def __init__(self, url: str):
        '''DB_connection class constructor.

        Constructor of DB_connection class.

        Args:
            url(str): URL of the database
        '''
        self._engine, self._session_maker = self._create_connection(url)
        self._declarative_base = self._create_orm_base()

    def __del__(self):
        '''DB_connection class destructor.

        Destructor for DB_connection class.
        '''
        self._destroy_connection()

    def _create_connection(
        self, database_url: str
    ) -> tuple[typing.Any, typing.Any]:
        '''Creates a new connection to the database.

        Creates SQLalchemy\'s engine and sessionmaker.

        Args:
            database_url(str): The url of the database

        Returns:
            SQLalchemy\'s engine and sessionmaker
        '''
        try:
            engine = sqlalchemy.create_engine(database_url)
            session = orm.sessionmaker(
                bind=engine,
                class_=orm.Session,
                expire_on_commit=False,
            )
            return engine, session
        except Exception:
            raise ConnectionError(
                f'Failed to establish connection to {database_url}',
            )

    def _destroy_connection(self):
        '''Destroy connection to database.'''
        self._engine.dispose()

    def _create_orm_base(self) -> orm.DeclarativeMetaData:
        '''Creates SQLAlchemy\'s declarative base.'''
        return orm.declarative_base()

    def get_base(self) -> orm.DeclarativeMetaData:
        '''sqlalchemy.orm.DeclarativeMetaData: returns SQLAlchemy\'s
        declarative base.'''
        return self._declarative_base

    def create_tables(self) -> None:
        '''Creates all tables'''
        with self._engine.begin() as conn:
            conn.run_sync(self._declarative_base.metadata.create_all)

    def drop_tables(self) -> None:
        '''Drops all tables'''
        with self._engine.begin() as conn:
            conn.run_sync(self._declarative_base.metadata.drop_all)
