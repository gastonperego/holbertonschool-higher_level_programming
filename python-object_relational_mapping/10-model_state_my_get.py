#!/usr/bin/python3
"""
This module uses SqlAlchemy to make a connection to
DataBase and print id of searched State name
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Session = sessionmaker(engine)
    session = Session()

    row = session.query(State).filter(State.name.like(state_name)).first()
    if row:
        print("{}".format(row.id))
    else:
        print("Not found")

    session.close()
