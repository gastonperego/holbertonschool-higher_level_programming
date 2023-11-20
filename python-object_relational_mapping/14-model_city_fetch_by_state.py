#!/usr/bin/python3
"""
    deletes all State objects with a name containing the letter
      a from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    table = session.query(State).join(City)
    for row in table:
        print(f"{row.State.name}: ({row.City.id}) {row.City.name}")
