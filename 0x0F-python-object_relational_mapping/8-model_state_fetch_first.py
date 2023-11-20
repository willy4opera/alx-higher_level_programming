#!/usr/bin/python3

""" Here, we print the first State object from the database hbtn_0e_6_usa
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
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
