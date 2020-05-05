#!/usr/bin/env python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String(255))

class Converter(Base):
    __tablename__ = 'converter'

    id = Column(Integer, primary_key=True)
    postcode = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)

class Church(Base):
    __tablename__ = 'churches'

    id = Column(Integer, primary_key=True)
    postcode = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    name = Column(String(255))
    website = Column(String(255))

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    postcode = Column(String(255))
    sex = Column(String(1))
    church = Column(String(255))

class User(Base):
    __tablename__ = 'users'

    email = Column(String(255), primary_key=True)
    password_hash = Column(String(255))

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    # Base.metadata.drop_all(engine)
    try:
        Base.metadata.create_all(engine)
    except(e):
        print(e)
