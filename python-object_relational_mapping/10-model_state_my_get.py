#!/usr/bin/python3
"""
    prints the State object with the name passed as argument
     from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Session = sessionmaker(engine)
    session = Session()
    rows = session.query(State)
    rows = rows.where(name == argv[4]).all()
    if rows:
        print(rows.id)
    else:
        print("Not found")
