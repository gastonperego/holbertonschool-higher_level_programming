#!/usr/bin/python3
"""
    that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    session = Session(engine)
    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)