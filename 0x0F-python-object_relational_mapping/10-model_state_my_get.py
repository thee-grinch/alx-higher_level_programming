#!/usr/bin/python3
"""this module queries from a database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    matched = argv[4]
    state = session.query(State).filter(
        State.name == matched).first()
    if state:
        print('{}'.format(state.id))
    else:
        print("Not found")

    session.close()
