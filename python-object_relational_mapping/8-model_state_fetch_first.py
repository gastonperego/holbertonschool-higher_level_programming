#!/usr/bin/python3
"""
    prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Session = sessionmaker(engine)
    session = Session()
    states_row = session.query(State).order_by(State.id).first()

    print(f"{states_row.id}: {states_row.name}")
