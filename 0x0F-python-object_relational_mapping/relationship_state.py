#!/usr/bin/python3

"""
Here, this script contains State class and Base,
an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

dev_metadata = MetaData()
Base = declarative_base(metadata=dev_metadata)


class State(Base):
    """
    Here, the class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
