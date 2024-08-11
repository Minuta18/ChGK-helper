from flask import Flask
from flask_httpauth import HTTPTokenAuth
import secrets
from sqlalchemy import orm
import sqlalchemy
import api
import typing_extensions


class Packages(api.orm_base):
    '''Packages model

    Model for packages of our app.

    Attributes:
        id (int): id of the package
        name (str): name of the package
        description (str): short description
        user_id (int): id of the creator
    '''
    __tablename__ = 'packages'

    id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, primary_key=True,
        autoincrement=True, unique=True,
    )
    name: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text, unique=True, nullable=False,
    )
    description: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text,
    )
    user_id: orm.Mapped[str] = orm.mapped_column(
        sqlalchemy.Text, nullable=False,
    )

    @staticmethod
    def get_package(package_id: int) -> typing_extensions.Self | None:
        '''Returns package by id or None if it not found'''
        session = api.db.get_session()
        return session.get(Packages, package_id)


class PackagesToQuestions(api.orm_base):
    '''Packages model

    Table of inventory of packages

    Attributes:
        package_id (int): id of the package
        question_id (int): id of the question
    '''
    __tablename__ = 'packages_to_questions'

    package_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Integer, nullable=False,
    )
    question_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.Text, nullable=False,
    )

    @staticmethod
    def get_questions_by_package_id(package_id) -> list[typing_extensions.Self]:
        '''Returns questions by package id'''
        session = api.db.get_session()
        return session.scalars(sqlalchemy.select(PackagesToQuestions).where(
            (PackagesToQuestions.package_id == package_id)
        )).all()