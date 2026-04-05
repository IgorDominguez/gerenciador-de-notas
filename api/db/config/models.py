from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Relationship
from db.config.connection import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Notes(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    date_time = Column(DateTime, default=datetime.datetime.now)

    user = Relationship('User', backref='notes', lazy='subquery')