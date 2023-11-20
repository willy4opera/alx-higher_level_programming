#!/usr/bin/python3

""" Here, we print the State object with the
name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    dev_eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dev_eng)
    Session = sessionmaker(bind=dev_eng)
    session = Session()
    n_state = State(name='Louisiana')
    session.add(n_state)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
