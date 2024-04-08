import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Income(SqlAlchemyBase):
    __tablename__ = 'incomes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    money = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime,
                             default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
