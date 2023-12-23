#!/usr/bin/python3
""" This model uses  an engine to query data
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import base, State


if __name__ == "__main__":

    DATABASE_URL = f"""mysql+mysqldb://{argv[1]}
    :{argv[2]}@localhost:3306/{argv[3]}"""

    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        print(f"{state.id}: {state.name}")
    session.close()
