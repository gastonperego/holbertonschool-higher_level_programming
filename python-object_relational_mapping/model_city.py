#!/usr/bin/python3
"""
     class definition of a City
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine


class City(Base):
    """
        Class City
    """
    __tablename__ = "cities"

    id = Column("id", Integer, unique=True, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'), nullable=False)