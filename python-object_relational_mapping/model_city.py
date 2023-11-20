#!/usr/bin/python3
"""
     class definition of a City
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, create_engine


class City(Base):
    """
        Class City
    """
    __tablename__ = "cities"

    id = Column("id", Integer, unique=True, autoincrement=True, 
                primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, nullable=False, ForeignKey("states.id"))