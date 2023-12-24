#!/usr/bin/python3
""" this script updates a query"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
    session.close()

