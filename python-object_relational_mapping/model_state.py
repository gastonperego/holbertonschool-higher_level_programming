#!/usr/bin/python3
"""
     class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()


class State(Base):
    """
        Class State
    """
    __tablename__ = "states"
    id = Column("id", Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)
