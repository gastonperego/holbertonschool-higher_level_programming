#!/usr/bin/python3
"""
    lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import query

if __name__ == "__main__":

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Session = sessionmaker(engine)
    session = Session()
    rows = session.query(State).order_by(state.id).all()
    i = 1
    for row in rows:
        print(f"{i}: {row.name}")
        i += 1
